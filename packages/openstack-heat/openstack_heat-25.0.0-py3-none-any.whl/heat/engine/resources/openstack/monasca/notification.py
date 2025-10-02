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

from heat.common.i18n import _
from heat.engine.resources.openstack.heat import none_resource
from heat.engine import support


class MonascaNotification(none_resource.NoneResource):
    """Heat Template Resource for Monasca Notification.

    A resource which is used to notificate if there is some alarm.
    Monasca Notification helps to declare the hook points, which will be
    invoked once alarm is generated. This plugin helps to create, update and
    delete the notification.
    """

    support_status = support.SupportStatus(
        version='25.0.0',
        status=support.HIDDEN,
        message=_('Monasca project was retired'),
        previous_status=support.SupportStatus(
            version='22.0.0',
            status=support.DEPRECATED,
            message=_('Monasca project was marked inactive'),
            previous_status=support.SupportStatus(
                version='7.0.0',
                status=support.SUPPORTED,
                previous_status=support.SupportStatus(
                    version='5.0.0',
                    status=support.SUPPORTED
                ))))


def resource_mapping():
    return {
        'OS::Monasca::Notification': MonascaNotification
    }
