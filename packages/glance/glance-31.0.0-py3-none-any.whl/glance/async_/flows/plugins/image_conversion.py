# Copyright 2018 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json
import os

from oslo_concurrency import processutils as putils
from oslo_config import cfg
from oslo_log import log as logging
from oslo_utils import excutils
from oslo_utils.imageutils import format_inspector
from taskflow.patterns import linear_flow as lf
from taskflow import task

from glance.async_ import utils
from glance.i18n import _, _LI

LOG = logging.getLogger(__name__)

conversion_plugin_opts = [
    cfg.StrOpt('output_format',
               default='raw',
               choices=('qcow2', 'raw', 'vmdk'),
               help=_("""
Desired output format for image conversion plugin.

Provide a valid image format to which the conversion plugin
will convert the image before storing it to the back-end.

Note, if the Image Conversion plugin for image import is defined, users
should only upload disk formats that are supported by `quemu-img` otherwise
the conversion and import will fail.

Possible values:
    * qcow2
    * raw
    * vmdk

Related Options:
    * disk_formats
""")),
]

CONF = cfg.CONF

CONF.register_opts(conversion_plugin_opts, group='image_conversion')


class _ConvertImage(task.Task):

    default_provides = 'file_path'

    def __init__(self, context, task_id, task_type, action_wrapper,
                 stores):
        self.context = context
        self.task_id = task_id
        self.task_type = task_type
        self.action_wrapper = action_wrapper
        self.stores = stores
        self.image_id = action_wrapper.image_id
        self.dest_path = ""
        self.src_path = ""
        self.python = CONF.wsgi.python_interpreter
        super(_ConvertImage, self).__init__(
            name='%s-Convert_Image-%s' % (task_type, task_id))

    def execute(self, file_path, **kwargs):
        with self.action_wrapper as action:
            return self._execute(action, file_path, **kwargs)

    def _inspect_path(self, path):
        """Return a FormatInspector for path.

        This encapsulates the act of inspecting a file, running safety checks,
        and raising/logging if anything goes wrong. If nothing fails, return
        the FileInspector for the file.
        """
        # Use our own cautious inspector module (if we have one for this
        # format) to make sure a file is the format the submitter claimed
        # it is and that it passes some basic safety checks _before_ we run
        # qemu-img on it.
        # See https://bugs.launchpad.net/nova/+bug/2059809 for details.
        try:
            inspector = format_inspector.detect_file_format(path)
            inspector.safety_check()
        except format_inspector.SafetyCheckFailed as e:
            nonfatal = set(CONF.image_format.gpt_safety_checks_nonfatal)
            fatal = e.failures.keys() - nonfatal
            if inspector.NAME == 'gpt' and not fatal:
                LOG.warning('Non-fatal %s', e)
            else:
                LOG.error('%s %s', str(inspector), e)
                raise RuntimeError('Image has disallowed configuration')
        except format_inspector.ImageFormatError as e:
            LOG.error('Image failed format inspection: %s', e)
            raise RuntimeError('Image format detection failed')
        except Exception as e:
            LOG.exception('Unknown error inspecting image format: %s', e)
            raise RuntimeError('Unable to inspect image')
        return inspector

    def _execute(self, action, file_path, **kwargs):

        target_format = CONF.image_conversion.output_format
        # TODO(jokke): Once we support other schemas we need to take them into
        # account and handle the paths here.
        self.src_path = file_path.split('file://')[-1]
        dest_path = "%(path)s.%(target)s" % {'path': self.src_path,
                                             'target': target_format}
        self.dest_path = dest_path
        source_format = action.image_disk_format
        inspector = self._inspect_path(self.src_path)

        detected_format = str(inspector)
        if detected_format == 'gpt':
            # FIXME(danms): We need to consider GPT to be raw for compatibility
            detected_format = 'raw'

        if detected_format == 'iso':
            if source_format == 'iso':
                # NOTE(abhishekk): Excluding conversion and preserving image
                # disk_format as `iso` only
                LOG.debug("Avoiding conversion of an image %s having"
                          " `iso` disk format.", self.image_id)
                return file_path

            # NOTE(abhishekk): Raising error as image detected as ISO but
            # claimed as different format
            LOG.error('Image claimed to be %s format but format '
                      'inspection found: ISO', source_format)
            raise RuntimeError("Image has disallowed configuration")
        elif detected_format != source_format:
            LOG.error('Image claimed to be %s format failed format '
                      'inspection', source_format)
            raise RuntimeError('Image format mismatch')

        try:
            stdout, stderr = putils.trycmd("qemu-img", "info",
                                           "-f", source_format,
                                           "--output=json",
                                           self.src_path,
                                           prlimit=utils.QEMU_IMG_PROC_LIMITS,
                                           python_exec=self.python,
                                           log_errors=putils.LOG_ALL_ERRORS,)
        except OSError as exc:
            with excutils.save_and_reraise_exception():
                msg = ("Failed to do introspection as part of image "
                       "conversion for %(iid)s: %(err)s")
                LOG.error(msg, {'iid': self.image_id, 'err': exc})

        if stderr:
            raise RuntimeError(stderr)

        metadata = json.loads(stdout)
        if metadata.get('format') != source_format:
            LOG.error('Image claiming to be %s reported as %s by qemu-img',
                      source_format, metadata.get('format', 'unknown'))
            raise RuntimeError('Image metadata disagrees about format')

        virtual_size = metadata.get('virtual-size', 0)
        action.set_image_attribute(virtual_size=virtual_size)

        if 'backing-filename' in metadata:
            LOG.warning('Refusing to process QCOW image with a backing file')
            raise RuntimeError(
                'QCOW images with backing files are not allowed')

        try:
            data_file = metadata['format-specific']['data']['data-file']
        except KeyError:
            data_file = None
        if data_file is not None:
            raise RuntimeError(
                'QCOW images with data-file set are not allowed')

        if metadata.get('format') == 'vmdk':
            create_type = metadata.get(
                'format-specific', {}).get(
                    'data', {}).get('create-type')
            allowed = CONF.image_format.vmdk_allowed_types
            if not create_type:
                raise RuntimeError(_('Unable to determine VMDK create-type'))
            if not len(allowed):
                LOG.warning(_('Refusing to process VMDK file as '
                              'vmdk_allowed_types is empty'))
                raise RuntimeError(_('Image is a VMDK, but no VMDK createType '
                                     'is specified'))
            if create_type not in allowed:
                LOG.warning(_('Refusing to process VMDK file with create-type '
                              'of %r which is not in allowed set of: %s'),
                            create_type, ','.join(allowed))
                raise RuntimeError(_('Invalid VMDK create-type specified'))

        if source_format == target_format:
            LOG.debug("Source is already in target format, "
                      "not doing conversion for %s", self.image_id)
            return file_path

        try:
            stdout, stderr = putils.trycmd('qemu-img', 'convert',
                                           '-f', source_format,
                                           '-O', target_format,
                                           self.src_path, dest_path,
                                           log_errors=putils.LOG_ALL_ERRORS)
        except OSError as exc:
            with excutils.save_and_reraise_exception():
                msg = "Failed to do image conversion for %(iid)s: %(err)s"
                LOG.error(msg, {'iid': self.image_id, 'err': exc})

        if stderr:
            raise RuntimeError(stderr)

        dest_inspector = self._inspect_path(dest_path)
        dest_format = str(dest_inspector)
        if dest_format == 'gpt':
            # FIXME(danms): We need to consider GPT to be raw for compatibility
            dest_format = 'raw'

        if target_format != dest_format:
            # If someone hid one format inside another, we should reject it
            # as we could be about to embed a vmdk in a 'raw' or similar.
            LOG.error('Image detected as %s after conversion to %s',
                      dest_format, target_format)
            raise RuntimeError('Converted image in unexpected format')
        action.set_image_attribute(disk_format=target_format,
                                   container_format='bare')
        new_size = os.stat(dest_path).st_size
        action.set_image_attribute(size=new_size)
        LOG.info(_LI('Updated image %s size=%i disk_format=%s'),
                 self.image_id, new_size, target_format)

        os.remove(self.src_path)

        return "file://%s" % dest_path

    def revert(self, result=None, **kwargs):
        # NOTE(flaper87): If result is None, it probably
        # means this task failed. Otherwise, we would have
        # a result from its execution.
        if result is not None:
            LOG.debug("Image conversion failed.")
            if os.path.exists(self.dest_path):
                os.remove(self.dest_path)

        # NOTE(abhishekk): If we failed to convert the image, then none
        # of the _ImportToStore() tasks could have run, so we need
        # to move all stores out of "importing" to "failed".
        with self.action_wrapper as action:
            action.set_image_attribute(status='queued')
            if self.stores:
                action.remove_importing_stores(self.stores)
                action.add_failed_stores(self.stores)

        if self.src_path:
            try:
                os.remove(self.src_path)
            except FileNotFoundError:
                # NOTE(abhishekk): We must have raced with something
                # else, so this is not a problem
                pass


def get_flow(**kwargs):
    """Return task flow for no-op.

    :param context: request context
    :param task_id: Task ID.
    :param task_type: Type of the task.
    :param image_repo: Image repository used.
    :param image_id: Image ID
    :param action_wrapper: An api_image_import.ActionWrapper.
    """
    context = kwargs.get('context')
    task_id = kwargs.get('task_id')
    task_type = kwargs.get('task_type')
    action_wrapper = kwargs.get('action_wrapper')
    stores = kwargs.get('backend', [])

    return lf.Flow(task_type).add(
        _ConvertImage(context, task_id, task_type, action_wrapper, stores)
    )
