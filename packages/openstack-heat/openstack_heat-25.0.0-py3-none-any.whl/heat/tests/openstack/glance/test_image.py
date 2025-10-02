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

from unittest import mock

from glanceclient import exc
from heat.common import exception
from heat.common import template_format
from heat.engine import stack as parser
from heat.engine import template
from heat.tests import common
from heat.tests import utils

image_download_template = '''
heat_template_version: rocky
description: This template to define a glance image.
resources:
  my_image:
    type: OS::Glance::WebImage
    properties:
      name: cirros_image
      id: 41f0e60c-ebb4-4375-a2b4-845ae8b9c995
      disk_format: qcow2
      container_format: bare
      min_disk: 10
      min_ram: 512
      protected: False
      location: https://launchpad.net/cirros/cirros-0.3.0-x86_64-disk.img
      architecture: test_architecture
      kernel_id: 12345678-1234-1234-1234-123456789012
      os_distro: test_distro
      owner: test_owner
      ramdisk_id: 12345678-1234-1234-1234-123456789012
'''

image_download_template_validate = '''
heat_template_version: rocky
description: This template to define a glance image.
resources:
  image:
    type: OS::Glance::WebImage
    properties:
      name: image_validate
      disk_format: qcow2
      container_format: bare
      location: https://launchpad.net/cirros/cirros-0.3.0-x86_64-disk.img
'''


class GlanceWebImageTest(common.HeatTestCase):
    def setUp(self):
        super(GlanceWebImageTest, self).setUp()

        self.ctx = utils.dummy_context()
        tpl = template_format.parse(image_download_template)
        self.stack = parser.Stack(
            self.ctx, 'glance_image_test_stack',
            template.Template(tpl)
        )

        self.my_image = self.stack['my_image']
        glance = mock.MagicMock()
        self.glanceclient = mock.MagicMock()
        self.my_image.client = glance
        glance.return_value = self.glanceclient
        self.images = self.glanceclient.images
        self.image_tags = self.glanceclient.image_tags
        self.image_members = self.glanceclient.image_members
        self.update = self.glanceclient.update

    def _test_validate(self, resource, error_msg):
        exc = self.assertRaises(exception.StackValidationFailed,
                                resource.validate)
        self.assertIn(error_msg, str(exc))

    def test_invalid_min_disk(self):
        # invalid 'min_disk'
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        props['min_disk'] = -1
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = ('Property error: resources.image.properties.min_disk: '
                     '-1 is out of range (min: 0, max: None)')
        self._test_validate(image, error_msg)

    def test_invalid_min_ram(self):
        # invalid 'min_ram'
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        props['min_ram'] = -1
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = ('Property error: resources.image.properties.min_ram: '
                     '-1 is out of range (min: 0, max: None)')
        self._test_validate(image, error_msg)

    def test_miss_disk_format(self):
        # miss disk_format
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        del props['disk_format']
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = 'Property disk_format not assigned'
        self._test_validate(image, error_msg)

    def test_invalid_disk_format(self):
        # invalid disk_format
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        props['disk_format'] = 'incorrect_format'
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = ('Property error: '
                     'resources.image.properties.disk_format: '
                     '"incorrect_format" is not an allowed value')
        self._test_validate(image, error_msg)

    def test_miss_container_format(self):
        # miss container_format
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        del props['container_format']
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = 'Property container_format not assigned'
        self._test_validate(image, error_msg)

    def test_invalid_container_format(self):
        # invalid container_format
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        props['container_format'] = 'incorrect_format'
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = ('Property error: '
                     'resources.image.properties.container_format: '
                     '"incorrect_format" is not an allowed value')
        self._test_validate(image, error_msg)

    def test_miss_location(self):
        # miss location
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        del props['location']
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = 'Property location not assigned'
        self._test_validate(image, error_msg)

    def test_invalid_disk_container_mix(self):
        tpl = template_format.parse(image_download_template_validate)
        stack = parser.Stack(
            self.ctx, 'glance_image_stack_validate',
            template.Template(tpl)
        )
        image = stack['image']
        props = stack.t.t['resources']['image']['properties'].copy()
        props['disk_format'] = 'raw'
        props['container_format'] = 'ari'
        image.t = image.t.freeze(properties=props)
        image.reparse()
        error_msg = ("Invalid mix of disk and container formats. When "
                     "setting a disk or container format to one of 'aki', "
                     "'ari', or 'ami', the container and disk formats must "
                     "match.")
        self._test_validate(image, error_msg)

    def test_image_handle_create(self):
        value = mock.MagicMock()
        image_id = '41f0e60c-ebb4-4375-a2b4-845ae8b9c995'
        value.id = image_id
        self.images.create.return_value = value
        self.image_tags.update.return_value = None
        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['tags'] = ['tag1']
        props['extra_properties'] = {"hw_firmware_type": "uefi"}
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        self.my_image.handle_create()

        self.assertEqual(image_id, self.my_image.resource_id)
        # assert that no tags pass when image create
        self.images.create.assert_called_once_with(
            architecture='test_architecture',
            container_format='bare',
            disk_format='qcow2',
            id='41f0e60c-ebb4-4375-a2b4-845ae8b9c995',
            kernel_id='12345678-1234-1234-1234-123456789012',
            os_distro='test_distro',
            ramdisk_id='12345678-1234-1234-1234-123456789012',
            visibility='private',
            min_disk=10,
            min_ram=512,
            name='cirros_image',
            protected=False,
            owner='test_owner',
            tags=['tag1']
        )
        self.images.update.assert_called_once_with(
            image_id, hw_firmware_type='uefi')

    def test_image_active_property_image_not_active(self):
        self.images.reactivate.return_value = None
        self.images.deactivate.return_value = None
        value = mock.MagicMock()
        image_id = '41f0e60c-ebb4-4375-a2b4-845ae8b9c995'
        value.id = image_id
        value.status = 'pending'
        self.images.create.return_value = value
        self.my_image.handle_create()
        self.my_image.check_create_complete(image_id)
        self.images.deactivate.assert_not_called()

    def test_image_active_property_image_active_to_deactivate(self):
        self.images.reactivate.return_value = None
        self.images.deactivate.return_value = None
        value = mock.MagicMock()
        image_id = '41f0e60c-ebb4-4375-a2b4-845ae8b9c995'
        value.id = image_id
        value.status = 'active'
        self.my_image.resource_id = image_id
        self.images.create.return_value = value
        self.images.get.return_value = value
        self.my_image.check_create_complete(False)
        self.images.deactivate.assert_called_once_with(
            self.my_image.resource_id)

    def test_image_active_property_image_status_killed(self):
        self.images.reactivate.return_value = None
        self.images.deactivate.return_value = None
        value = mock.MagicMock()
        image_id = '41f0e60c-ebb4-4375-a2b4-845ae8b9c995'
        value.id = image_id
        value.status = 'killed'
        self.my_image.resource_id = image_id
        self.images.create.return_value = value
        self.images.get.return_value = value
        ex = self.assertRaises(exception.ResourceInError,
                               self.my_image.check_create_complete, False)
        self.assertIn('killed', ex.message)

    def _handle_update_image_props(self, prop_diff):
        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)
        self.images.update.assert_called_once_with(
            self.my_image.resource_id,
            ['hw_firmware_type'],
            os_secure_boot='required'
        )

    def _handle_update_tags(self, prop_diff):
        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)

        self.image_tags.update.assert_called_once_with(
            self.my_image.resource_id,
            'tag2'
        )
        self.image_tags.delete.assert_called_once_with(
            self.my_image.resource_id,
            'tag1'
        )

    def test_image_handle_update(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'
        prop_diff = {
            'architecture': 'test_architecture',
            'kernel_id': '12345678-1234-1234-1234-123456789012',
            'os_distro': 'test_distro',
            'owner': 'test_owner',
            'ramdisk_id': '12345678-1234-1234-1234-123456789012'}

        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)
        self.images.update.assert_called_with(
            self.my_image.resource_id,
            architecture='test_architecture',
            kernel_id='12345678-1234-1234-1234-123456789012',
            os_distro='test_distro',
            owner='test_owner',
            ramdisk_id='12345678-1234-1234-1234-123456789012'
        )

    def test_image_handle_update_deactivate(self):
        self.images.reactivate.return_value = None
        self.images.deactivate.return_value = None
        value = mock.MagicMock()
        image_id = '41f0e60c-ebb4-4375-a2b4-845ae8b9c995'
        value.id = image_id
        value.status = 'active'
        self.my_image.resource_id = image_id
        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['active'] = False
        self.my_image.t = self.my_image.t.freeze(properties=props)
        prop_diff = {'active': False}
        self.my_image.reparse()
        self.images.update.return_value = value
        self.images.get.return_value = value
        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)
        self.images.deactivate.assert_called_once_with(
            self.my_image.resource_id)

    def test_image_handle_update_reactivate(self):
        self.images.reactivate.return_value = None
        self.images.deactivate.return_value = None
        value = mock.MagicMock()
        image_id = '41f0e60c-ebb4-4375-a2b4-845ae8b9c995'
        value.id = image_id
        value.status = 'deactivated'
        self.my_image.resource_id = image_id
        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['active'] = True
        self.my_image.t = self.my_image.t.freeze(properties=props)
        prop_diff = {'active': True}
        self.my_image.reparse()
        self.images.update.return_value = value
        self.images.get.return_value = value
        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)
        self.my_image.check_update_complete(True)
        self.images.reactivate.assert_called_once_with(
            self.my_image.resource_id)

    def test_image_handle_update_image_props(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'

        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['extra_properties'] = {"hw_firmware_type": "uefi"}
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        prop_diff = {'extra_properties': {"os_secure_boot": "required"}}

        self._handle_update_image_props(prop_diff)

    def test_image_handle_update_tags(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'

        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['tags'] = ['tag1']
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        prop_diff = {'tags': ['tag2']}

        self._handle_update_tags(prop_diff)

    def test_image_handle_update_remove_tags(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'

        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['tags'] = ['tag1']
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        prop_diff = {'tags': None}

        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)

        self.image_tags.delete.assert_called_once_with(
            self.my_image.resource_id,
            'tag1'
        )

    def _handle_update_members(self, prop_diff):
        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)

        self.image_members.create.assert_called_once_with(
            self.my_image.resource_id,
            'member2'
        )
        self.image_members.delete.assert_called_once_with(
            self.my_image.resource_id,
            'member1'
        )

    def test_image_handle_update_members(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'

        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['members'] = ['member1']
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        prop_diff = {'members': ['member2']}

        self._handle_update_members(prop_diff)

    def test_image_handle_update_remove_members(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'

        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['members'] = ['member1']
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        prop_diff = {'members': None}

        self.my_image.handle_update(json_snippet=None,
                                    tmpl_diff=None,
                                    prop_diff=prop_diff)

        self.image_members.delete.assert_called_once_with(
            self.my_image.resource_id,
            'member1'
        )

    def test_image_handle_update_tags_delete_not_found(self):
        self.my_image.resource_id = '477e8273-60a7-4c41-b683-fdb0bc7cd151'

        props = self.stack.t.t['resources']['my_image']['properties'].copy()
        props['tags'] = ['tag1']
        self.my_image.t = self.my_image.t.freeze(properties=props)
        self.my_image.reparse()
        prop_diff = {'tags': ['tag2']}

        self.image_tags.delete.side_effect = exc.HTTPNotFound()

        self._handle_update_tags(prop_diff)

    def test_image_show_resource_v1(self):
        self.glanceclient.version = 1.0
        self.my_image.resource_id = 'test_image_id'
        image = mock.MagicMock()
        images = mock.MagicMock()
        image.to_dict.return_value = {'image': 'info'}
        images.get.return_value = image
        self.my_image.client().images = images
        self.assertEqual({'image': 'info'}, self.my_image.FnGetAtt('show'))
        images.get.assert_called_once_with('test_image_id')

    def test_image_show_resource_v2(self):
        self.my_image.resource_id = 'test_image_id'
        # glance image in v2 is warlock.model object, so it can be
        # handled via dict(). In test we use easiest analog - dict.
        image = {"key1": "val1", "key2": "val2"}
        self.images.get.return_value = image
        self.glanceclient.version = 2.0
        self.assertEqual({"key1": "val1", "key2": "val2"},
                         self.my_image.FnGetAtt('show'))
        self.images.get.assert_called_once_with('test_image_id')

    def test_image_get_live_state_v2(self):
        self.glanceclient.version = 2.0
        self.my_image.resource_id = '1234'
        images = mock.MagicMock()
        show_value = {
            'name': 'test',
            'disk_format': 'qcow2',
            'container_format': 'bare',
            'active': None,
            'protected': False,
            'is_public': False,
            'min_disk': 0,
            'min_ram': 0,
            'id': '41f0e60c-ebb4-4375-a2b4-845ae8b9c995',
            'tags': [],
            'architecture': 'test_architecture',
            'kernel_id': '12345678-1234-1234-1234-123456789012',
            'os_distro': 'test_distro',
            'os_version': '1.0',
            'owner': 'test_owner',
            'ramdisk_id': '12345678-1234-1234-1234-123456789012',
            'members': None,
            'visibility': 'private'
        }
        image = show_value
        images.get.return_value = image
        self.my_image.client().images = images

        reality = self.my_image.get_live_state(self.my_image.properties)
        expected = {
            'name': 'test',
            'disk_format': 'qcow2',
            'container_format': 'bare',
            'active': None,
            'protected': False,
            'min_disk': 0,
            'min_ram': 0,
            'id': '41f0e60c-ebb4-4375-a2b4-845ae8b9c995',
            'tags': [],
            'architecture': 'test_architecture',
            'kernel_id': '12345678-1234-1234-1234-123456789012',
            'os_distro': 'test_distro',
            'os_version': '1.0',
            'owner': 'test_owner',
            'ramdisk_id': '12345678-1234-1234-1234-123456789012',
            'members': None,
            'visibility': 'private'
        }

        self.assertEqual(set(expected.keys()), set(reality.keys()))
        for key in expected:
            self.assertEqual(expected[key], reality[key])

    def test_get_live_state_resource_is_deleted(self):
        self.my_image.resource_id = '1234'
        self.my_image.client().images.get.return_value = {'status': 'deleted'}
        self.assertRaises(exception.EntityNotFound,
                          self.my_image.get_live_state,
                          self.my_image.properties)

    def test_parse_live_resource_data(self):
        resource_data = {
            'name': 'test',
            'disk_format': 'qcow2',
            'container_format': 'bare',
            'active': None,
            'protected': False,
            'is_public': False,
            'min_disk': 0,
            'min_ram': 0,
            'id': '41f0e60c-ebb4-4375-a2b4-845ae8b9c995',
            'tags': [],
            'architecture': 'test_architecture',
            'kernel_id': '12345678-1234-1234-1234-123456789012',
            'os_distro': 'new_distro',
            'os_version': '1.0',
            'os_secure_boot': 'False',
            'owner': 'new_owner',
            'hw_firmware_type': 'uefi',
            'ramdisk_id': '12345678-1234-1234-1234-123456789012',
            'members': None,
            'visibility': 'private'
        }

        resource_properties = self.stack.t.t['resources'][
            'my_image']['properties'].copy()
        resource_properties['extra_properties'] = {
            'hw_firmware_type': 'uefi',
            'os_secure_boot': 'required',
            }

        reality = self.my_image.parse_live_resource_data(resource_properties,
                                                         resource_data)
        expected = {
            'name': 'test',
            'disk_format': 'qcow2',
            'container_format': 'bare',
            'active': None,
            'protected': False,
            'min_disk': 0,
            'min_ram': 0,
            'id': '41f0e60c-ebb4-4375-a2b4-845ae8b9c995',
            'tags': [],
            'architecture': 'test_architecture',
            'kernel_id': '12345678-1234-1234-1234-123456789012',
            'os_distro': 'new_distro',
            'os_version': '1.0',
            'owner': 'new_owner',
            'ramdisk_id': '12345678-1234-1234-1234-123456789012',
            'members': None,
            'visibility': 'private',
            'extra_properties': {
                'hw_firmware_type': 'uefi',
                'os_secure_boot': 'False',
            }
        }

        self.assertEqual(set(expected.keys()), set(reality.keys()))
        for key in expected:
            self.assertEqual(expected[key], reality[key])
        for key in expected['extra_properties']:
            self.assertEqual(expected['extra_properties'][key],
                             reality['extra_properties'][key])
