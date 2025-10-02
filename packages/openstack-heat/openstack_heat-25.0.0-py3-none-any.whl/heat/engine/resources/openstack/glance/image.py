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

from heat.common import exception
from heat.common.i18n import _
from heat.engine import constraints
from heat.engine import properties
from heat.engine import resource
from heat.engine.resources.openstack.heat import none_resource
from heat.engine import support


class GlanceWebImage(resource.Resource):
    """A resource managing images in Glance using web-download import.

    This provides image support for recent Glance installation.
    """

    support_status = support.SupportStatus(version='12.0.0')

    PROPERTIES = (
        NAME, IMAGE_ID, MIN_DISK, MIN_RAM, PROTECTED,
        DISK_FORMAT, CONTAINER_FORMAT, LOCATION, TAGS,
        ARCHITECTURE, KERNEL_ID, OS_DISTRO, OS_VERSION, OWNER,
        EXTRA_PROPERTIES, VISIBILITY, RAMDISK_ID, ACTIVE, MEMBERS
    ) = (
        'name', 'id', 'min_disk', 'min_ram', 'protected',
        'disk_format', 'container_format', 'location', 'tags',
        'architecture', 'kernel_id', 'os_distro', 'os_version',
        'owner', 'extra_properties', 'visibility', 'ramdisk_id',
        'active', 'members'
    )

    glance_id_pattern = ('^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}'
                         '-([0-9a-fA-F]){4}-([0-9a-fA-F]){12}$')

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('Name for the image. The name of an image is not '
              'unique to a Image Service node.')
        ),
        IMAGE_ID: properties.Schema(
            properties.Schema.STRING,
            _('The image ID. Glance will generate a UUID if not specified.')
        ),
        MIN_DISK: properties.Schema(
            properties.Schema.INTEGER,
            _('Amount of disk space (in GB) required to boot image. '
              'Default value is 0 if not specified '
              'and means no limit on the disk size.'),
            constraints=[
                constraints.Range(min=0),
            ],
            default=0
        ),
        MIN_RAM: properties.Schema(
            properties.Schema.INTEGER,
            _('Amount of ram (in MB) required to boot image. Default value '
              'is 0 if not specified and means no limit on the ram size.'),
            constraints=[
                constraints.Range(min=0),
            ],
            default=0
        ),
        PROTECTED: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Whether the image can be deleted. If the value is True, '
              'the image is protected and cannot be deleted.'),
            update_allowed=True,
            default=False
        ),
        DISK_FORMAT: properties.Schema(
            properties.Schema.STRING,
            _('Disk format of image.'),
            required=True,
            constraints=[
                constraints.AllowedValues(
                    ['ami', 'ari', 'aki', 'vhd', 'vhdx', 'vmdk', 'raw',
                     'qcow2', 'vdi', 'iso', 'ploop'])
            ]
        ),
        CONTAINER_FORMAT: properties.Schema(
            properties.Schema.STRING,
            _('Container format of image.'),
            required=True,
            constraints=[
                constraints.AllowedValues([
                    'ami', 'ari', 'aki', 'bare', 'ovf', 'ova', 'docker'])
            ]
        ),
        LOCATION: properties.Schema(
            properties.Schema.STRING,
            _('URL where the data for this image already resides. For '
              'example, if the image data is stored in swift, you could '
              'specify "swift://example.com/container/obj".'),
            required=True,
        ),
        TAGS: properties.Schema(
            properties.Schema.LIST,
            _('List of image tags.'),
            update_allowed=True,
        ),
        ARCHITECTURE: properties.Schema(
            properties.Schema.STRING,
            _('Operating system architecture.'),
            update_allowed=True,
        ),
        KERNEL_ID: properties.Schema(
            properties.Schema.STRING,
            _('ID of image stored in Glance that should be used as '
              'the kernel when booting an AMI-style image.'),
            update_allowed=True,
            constraints=[
                constraints.AllowedPattern(glance_id_pattern)
            ]
        ),
        OS_DISTRO: properties.Schema(
            properties.Schema.STRING,
            _('The common name of the operating system distribution '
              'in lowercase.'),
            update_allowed=True,
        ),
        OS_VERSION: properties.Schema(
            properties.Schema.STRING,
            _('Operating system version as specified by the distributor.'),
            update_allowed=True,
        ),
        OWNER: properties.Schema(
            properties.Schema.STRING,
            _('Owner of the image.'),
            update_allowed=True,
        ),
        EXTRA_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('Arbitrary properties to associate with the image.'),
            update_allowed=True,
            default={},
            support_status=support.SupportStatus(version='17.0.0')
        ),
        VISIBILITY: properties.Schema(
            properties.Schema.STRING,
            _('Scope of image accessibility.'),
            update_allowed=True,
            default='private',
            constraints=[
                constraints.AllowedValues(
                    ['public', 'private', 'community', 'shared'])
            ]
        ),
        RAMDISK_ID: properties.Schema(
            properties.Schema.STRING,
            _('ID of image stored in Glance that should be used as '
              'the ramdisk when booting an AMI-style image.'),
            update_allowed=True,
            constraints=[
                constraints.AllowedPattern(glance_id_pattern)
            ]
        ),
        ACTIVE: properties.Schema(
            properties.Schema.BOOLEAN,
            _('Activate or deactivate the image. Requires Admin Access.'),
            default=True,
            update_allowed=True,
            support_status=support.SupportStatus(version='16.0.0')
        ),
        MEMBERS: properties.Schema(
            properties.Schema.LIST,
            _('List of additional members that are permitted '
              'to read the image. This may be a Keystone Project '
              'IDs or User IDs, depending on the Glance configuration '
              'in use.'),
            schema=properties.Schema(
                properties.Schema.STRING,
                _('A member ID. This may be a Keystone Project ID '
                  'or User ID, depending on the Glance configuration '
                  'in use.')
            ),
            update_allowed=True,
            support_status=support.SupportStatus(version='16.0.0')
        )
    }

    default_client_name = 'glance'

    entity = 'images'

    def handle_create(self):
        args = dict((k, v) for k, v in self.properties.items()
                    if v is not None and k is not self.EXTRA_PROPERTIES)
        members = args.pop(self.MEMBERS, [])
        active = args.pop(self.ACTIVE)
        location = args.pop(self.LOCATION)
        images = self.client().images
        image = images.create(**args)
        image_id = image.id
        self.resource_id_set(image_id)
        images.image_import(image_id, method='web-download', uri=location)
        for member in members:
            self.client().image_members.create(image_id, member)
        props = self.properties.get(self.EXTRA_PROPERTIES)
        images.update(image.id, **props)
        return active

    def check_create_complete(self, active):
        image = self.client().images.get(self.resource_id)
        if image.status == 'killed':
            raise exception.ResourceInError(
                resource_status=image.status,
            )
        if not active:
            if image.status == 'active':
                self.client().images.deactivate(self.resource_id)
                return True
            elif image.status == 'deactivated':
                return True
            else:
                return False
        else:
            return image.status == 'active'

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        images = self.client().images
        if prop_diff:
            active = prop_diff.pop(self.ACTIVE, None)
            if active is False:
                images.deactivate(self.resource_id)

            if self.TAGS in prop_diff:
                existing_tags = self.properties.get(self.TAGS) or []
                diff_tags = prop_diff.pop(self.TAGS) or []

                new_tags = set(diff_tags) - set(existing_tags)
                for tag in new_tags:
                    self.client().image_tags.update(
                        self.resource_id,
                        tag)

                removed_tags = set(existing_tags) - set(diff_tags)
                for tag in removed_tags:
                    with self.client_plugin().ignore_not_found:
                        self.client().image_tags.delete(
                            self.resource_id,
                            tag)

        if self.EXTRA_PROPERTIES in prop_diff:
            old_properties = self.properties.get(self.EXTRA_PROPERTIES)
            new_properties = prop_diff.pop(self.EXTRA_PROPERTIES)
            prop_diff.update(new_properties)
            remove_props = list(set(old_properties) - set(new_properties))

            # Though remove_props defaults to None within the glanceclient,
            # setting it to a list (possibly []) every time ensures only one
            # calling format to images.update
            images.update(self.resource_id, remove_props, **prop_diff)
        else:
            images.update(self.resource_id, **prop_diff)

            if self.MEMBERS in prop_diff:
                existing_members = self.properties.get(self.MEMBERS) or []
                diff_members = prop_diff.pop(self.MEMBERS) or []

                new_members = set(diff_members) - set(existing_members)
                for _member in new_members:
                    self.glance().image_members.create(
                        self.resource_id, _member)
                removed_members = set(existing_members) - set(diff_members)
                for _member in removed_members:
                    self.glance().image_members.delete(
                        self.resource_id, _member)

        return active

    def check_update_complete(self, active):
        if active:
            self.client().images.reactivate(self.resource_id)
        return True

    def validate(self):
        super(GlanceWebImage, self).validate()
        container_format = self.properties[self.CONTAINER_FORMAT]
        if (container_format in ['ami', 'ari', 'aki']
                and self.properties[self.DISK_FORMAT] != container_format):
            msg = _("Invalid mix of disk and container formats. When "
                    "setting a disk or container format to one of 'aki', "
                    "'ari', or 'ami', the container and disk formats must "
                    "match.")
            raise exception.StackValidationFailed(message=msg)

        if (self.properties[self.MEMBERS]
                and self.properties[self.VISIBILITY] != 'shared'):
            raise exception.ResourcePropertyValueDependency(
                prop1=self.MEMBERS,
                prop2=self.VISIBILITY,
                value='shared')

    def get_live_resource_data(self):
        image_data = super(GlanceWebImage, self).get_live_resource_data()
        if image_data.get('status') in ('deleted', 'killed'):
            raise exception.EntityNotFound(entity='Resource',
                                           name=self.name)
        return image_data

    def parse_live_resource_data(self, resource_properties, resource_data):
        image_reality = {}

        for key in self.PROPERTIES:
            if key == self.LOCATION:
                continue
            if key == self.IMAGE_ID:
                if (resource_properties.get(self.IMAGE_ID) is not None or
                        resource_data.get(self.IMAGE_ID) != self.resource_id):
                    image_reality.update({self.IMAGE_ID: resource_data.get(
                        self.IMAGE_ID)})
                else:
                    image_reality.update({self.IMAGE_ID: None})

            if key == self.EXTRA_PROPERTIES:
                continue
            else:
                image_reality.update({key: resource_data.get(key)})

        if resource_properties.get(self.EXTRA_PROPERTIES):
            extra_properties = {}
            for key in resource_properties.get(self.EXTRA_PROPERTIES):
                extra_properties[key] = resource_data.get(key)
            image_reality.update({self.EXTRA_PROPERTIES: extra_properties})

        return image_reality


class GlanceImage(none_resource.NoneResource):
    """A resource managing images in Glance.

    A resource provides managing images that are meant to be used with other
    services.
    """

    support_status = support.SupportStatus(
        status=support.HIDDEN,
        version='22.0.0',
        previous_status=support.SupportStatus(
            status=support.DEPRECATED,
            version='8.0.0',
            message=_(
                'Creating a Glance Image based on an existing URL location '
                'requires the Glance v1 API, which is deprecated.'),
            previous_status=support.SupportStatus(version='2014.2')
        )
    )


def resource_mapping():
    return {
        'OS::Glance::Image': GlanceImage,
        'OS::Glance::WebImage': GlanceWebImage
    }
