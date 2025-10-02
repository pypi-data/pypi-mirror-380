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

import os

from heatclient import client as heat_client
from keystoneauth1.identity.generic import password
from keystoneauth1 import session
from keystoneclient.v3 import client as kc_v3
from novaclient import client as nova_client
from swiftclient import client as swift_client


class KeystoneWrapperClient(object):
    """Wrapper object for keystone client

    This wraps keystone client, so we can encpasulate certain
    added properties like auth_token, project_id etc.
    """
    def __init__(self, auth_plugin, verify=True):
        self.auth_plugin = auth_plugin
        self.session = session.Session(
            auth=auth_plugin,
            verify=verify)

    @property
    def auth_token(self):
        return self.auth_plugin.get_token(self.session)

    @property
    def auth_ref(self):
        return self.auth_plugin.get_access(self.session)

    @property
    def project_id(self):
        return self.auth_plugin.get_project_id(self.session)

    def get_endpoint_url(self, service_type, region=None):
        kwargs = {
            'service_type': service_type,
            'region_name': region}
        return self.auth_ref.service_catalog.url_for(**kwargs)


class ClientManager(object):
    """Provides access to the official python clients for calling various APIs.

    Manager that provides access to the official python clients for
    calling various OpenStack APIs.
    """

    HEAT_API_VERSION = '1'
    KEYSTONE_API_VERSION = '3'
    NOVA_API_VERSION = '2.1'

    def __init__(self, conf, admin_credentials=False):
        self.conf = conf
        self.admin_credentials = admin_credentials

        self.insecure = self.conf.disable_ssl_certificate_validation
        self.ca_file = self.conf.ca_file

        self.identity_client = self._get_identity_client()
        self.keystone_client = self._get_keystone_client()
        self.orchestration_client = self._get_orchestration_client()
        self.compute_client = self._get_compute_client()
        self.object_client = self._get_object_client()

    def _username(self):
        if self.admin_credentials:
            return self.conf.admin_username
        return self.conf.username

    def _password(self):
        if self.admin_credentials:
            return self.conf.admin_password
        return self.conf.password

    def _project_name(self):
        if self.admin_credentials:
            return self.conf.admin_project_name
        return self.conf.project_name

    def _get_orchestration_client(self):
        endpoint = os.environ.get('HEAT_URL')
        if os.environ.get('OS_NO_CLIENT_AUTH') == 'True':
            session = None
        else:
            session = self.identity_client.session

        return heat_client.Client(
            self.HEAT_API_VERSION,
            endpoint,
            session=session,
            endpoint_type='publicURL',
            service_type='orchestration',
            region_name=self.conf.region,
            username=self._username(),
            password=self._password())

    def _get_identity_client(self):
        user_domain_id = self.conf.user_domain_id
        project_domain_id = self.conf.project_domain_id
        user_domain_name = self.conf.user_domain_name
        project_domain_name = self.conf.project_domain_name
        kwargs = {
            'username': self._username(),
            'password': self._password(),
            'project_name': self._project_name(),
            'auth_url': self.conf.auth_url,
            'user_domain_id': user_domain_id,
            'project_domain_id': project_domain_id,
            'user_domain_name': user_domain_name,
            'project_domain_name': project_domain_name
        }
        auth = password.Password(**kwargs)
        if self.insecure:
            verify_cert = False
        else:
            verify_cert = self.ca_file or True

        return KeystoneWrapperClient(auth, verify_cert)

    def _get_keystone_client(self):
        # Create our default Keystone client to use in testing
        return kc_v3.Client(
            session=self.identity_client.session,
            interface='publicURL',
            region_name=self.conf.region)

    def _get_compute_client(self):
        # Create our default Nova client to use in testing
        return nova_client.Client(
            self.NOVA_API_VERSION,
            session=self.identity_client.session,
            service_type='compute',
            endpoint_type='publicURL',
            region_name=self.conf.region,
            os_cache=False,
            http_log_debug=True)

    def _get_object_client(self):
        args = {
            'auth_version': self.KEYSTONE_API_VERSION,
            'session': self.identity_client.session,
            'os_options': {'endpoint_type': 'publicURL',
                           'region_name': self.conf.region,
                           'service_type': 'object-store'},
        }
        return swift_client.Connection(**args)
