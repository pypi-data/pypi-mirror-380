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

from oslo_log import log as logging

from heat.common import exception
from heat.common.i18n import _
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
from heat.engine.resources.openstack.neutron import neutron
from heat.engine.resources.openstack.neutron import port
from heat.engine.resources.openstack.neutron import router
from heat.engine import support
from heat.engine import translation

LOG = logging.getLogger(__name__)


class FloatingIP(neutron.NeutronResource):
    """A resource for managing Neutron floating ips.

    Floating IP addresses can change their association between routers by
    action of the user. One of the most common use cases for floating IPs is
    to provide public IP addresses to a private cloud, where there are a
    limited number of IP addresses available. Another is for a public cloud
    user to have a "static" IP address that can be reassigned when an instance
    is upgraded or moved.
    """

    entity = 'floatingip'

    PROPERTIES = (
        FLOATING_NETWORK_ID, FLOATING_NETWORK, FLOATING_SUBNET,
        VALUE_SPECS, PORT_ID, FIXED_IP_ADDRESS, FLOATING_IP_ADDRESS,
        DNS_NAME, DNS_DOMAIN,
    ) = (
        'floating_network_id', 'floating_network', 'floating_subnet',
        'value_specs', 'port_id', 'fixed_ip_address', 'floating_ip_address',
        'dns_name', 'dns_domain',
    )

    ATTRIBUTES = (
        ROUTER_ID, TENANT_ID, FLOATING_NETWORK_ID_ATTR, FIXED_IP_ADDRESS_ATTR,
        FLOATING_IP_ADDRESS_ATTR, PORT_ID_ATTR,
    ) = (
        'router_id', 'tenant_id', 'floating_network_id', 'fixed_ip_address',
        'floating_ip_address', 'port_id',
    )

    properties_schema = {
        FLOATING_NETWORK_ID: properties.Schema(
            properties.Schema.STRING,
            support_status=support.SupportStatus(
                status=support.HIDDEN,
                version='5.0.0',
                message=_('Use property %s.') % FLOATING_NETWORK,
                previous_status=support.SupportStatus(
                    status=support.DEPRECATED,
                    version='2014.2'
                )
            ),
            constraints=[
                constraints.CustomConstraint('neutron.network')
            ],
        ),
        FLOATING_NETWORK: properties.Schema(
            properties.Schema.STRING,
            _('Network to allocate floating IP from.'),
            support_status=support.SupportStatus(version='2014.2'),
            required=True,
            constraints=[
                constraints.CustomConstraint('neutron.network')
            ],
        ),
        FLOATING_SUBNET: properties.Schema(
            properties.Schema.STRING,
            _('Subnet to allocate floating IP from.'),
            support_status=support.SupportStatus(version='9.0.0'),
            constraints=[
                constraints.CustomConstraint('neutron.subnet')
            ],
        ),
        VALUE_SPECS: properties.Schema(
            properties.Schema.MAP,
            _('Extra parameters to include in the "floatingip" object in the '
              'creation request. Parameters are often specific to installed '
              'hardware or extensions.'),
            default={}
        ),
        PORT_ID: properties.Schema(
            properties.Schema.STRING,
            _('ID of an existing port with at least one IP address to '
              'associate with this floating IP.'),
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('neutron.port')
            ]
        ),
        FIXED_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('IP address to use if the port has multiple addresses.'),
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('ip_addr')
            ]
        ),
        FLOATING_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('IP address of the floating IP. NOTE: The default policy '
              'setting in Neutron restricts usage of this property to '
              'administrative users only.'),
            constraints=[
                constraints.CustomConstraint('ip_addr')
            ],
            support_status=support.SupportStatus(version='5.0.0'),
        ),
        DNS_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DNS name associated with floating ip.'),
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('rel_dns_name')
            ],
            support_status=support.SupportStatus(version='7.0.0'),
        ),
        DNS_DOMAIN: properties.Schema(
            properties.Schema.STRING,
            _('DNS domain associated with floating ip.'),
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('dns_domain')
            ],
            support_status=support.SupportStatus(version='7.0.0'),
        ),
    }

    attributes_schema = {
        ROUTER_ID: attributes.Schema(
            _('ID of the router used as gateway, set when associated with a '
              'port.'),
            type=attributes.Schema.STRING
        ),
        TENANT_ID: attributes.Schema(
            _('The tenant owning this floating IP.'),
            type=attributes.Schema.STRING
        ),
        FLOATING_NETWORK_ID_ATTR: attributes.Schema(
            _('ID of the network in which this IP is allocated.'),
            type=attributes.Schema.STRING
        ),
        FIXED_IP_ADDRESS_ATTR: attributes.Schema(
            _('IP address of the associated port, if specified.'),
            type=attributes.Schema.STRING,
            cache_mode=attributes.Schema.CACHE_NONE
        ),
        FLOATING_IP_ADDRESS_ATTR: attributes.Schema(
            _('The allocated address of this IP.'),
            type=attributes.Schema.STRING
        ),
        PORT_ID_ATTR: attributes.Schema(
            _('ID of the port associated with this IP.'),
            type=attributes.Schema.STRING,
            cache_mode=attributes.Schema.CACHE_NONE
        ),
    }

    def translation_rules(self, props):
        client_plugin = self.client_plugin()
        return [
            translation.TranslationRule(
                props,
                translation.TranslationRule.REPLACE,
                [self.FLOATING_NETWORK],
                value_path=[self.FLOATING_NETWORK_ID]
            ),
            translation.TranslationRule(
                props,
                translation.TranslationRule.RESOLVE,
                [self.FLOATING_NETWORK],
                client_plugin=client_plugin,
                finder='find_resourceid_by_name_or_id',
                entity=client_plugin.RES_TYPE_NETWORK
            ),
            translation.TranslationRule(
                props,
                translation.TranslationRule.RESOLVE,
                [self.FLOATING_SUBNET],
                client_plugin=client_plugin,
                finder='find_resourceid_by_name_or_id',
                entity=client_plugin.RES_TYPE_SUBNET
            )
        ]

    def _add_router_interface_dependencies(self, deps, resource):
        def port_on_subnet(resource, subnet):
            if not resource.has_interface('OS::Neutron::Port'):
                return False

            try:
                fixed_ips = resource.properties.get(port.Port.FIXED_IPS)
            except (ValueError, TypeError):
                # Properties errors will be caught later in validation, where
                # we can report them in their proper context.
                return False
            if not fixed_ips:
                # During create we have only unresolved value for
                # functions, so can not use None value for building
                # correct dependencies. Depend on all RouterInterfaces
                # when the port has no fixed IP specified, since we
                # can't safely assume that any are in different
                # networks.
                if subnet is None:
                    return True

                try:
                    p_net = (resource.properties.get(port.Port.NETWORK) or
                             resource.properties.get(port.Port.NETWORK_ID))
                except (ValueError, TypeError):
                    # Properties errors will be caught later in validation,
                    # where we can report them in their proper context.
                    return False
                if p_net:
                    try:
                        network = self.client().show_network(p_net)['network']
                        return subnet in network['subnets']
                    except Exception as exc:
                        LOG.info("Ignoring Neutron error while "
                                 "getting FloatingIP dependencies: %s",
                                 str(exc))
                        return False
            else:
                try:
                    fixed_ips = resource.properties.get(port.Port.FIXED_IPS)
                except (ValueError, TypeError):
                    # Properties errors will be caught later in validation,
                    # where we can report them in their proper context.
                    return False
                for fixed_ip in fixed_ips:
                    port_subnet = (fixed_ip.get(port.Port.FIXED_IP_SUBNET) or
                                   fixed_ip.get(port.Port.FIXED_IP_SUBNET_ID))
                    if subnet == port_subnet:
                        return True
            return False

        interface_subnet = (
            resource.properties.get(router.RouterInterface.SUBNET) or
            resource.properties.get(router.RouterInterface.SUBNET_ID))
        for d in deps.graph()[self]:
            if port_on_subnet(d, interface_subnet):
                deps += (self, resource)
                break

    def add_dependencies(self, deps):
        super(FloatingIP, self).add_dependencies(deps)

        for resource in self.stack.values():
            # depend on any RouterGateway in this template with the same
            # network_id as this floating_network_id
            if resource.has_interface('OS::Neutron::RouterGateway'):
                try:
                    gateway_network = (
                        resource.properties.get(router.RouterGateway.NETWORK)
                        or resource.properties.get(
                            router.RouterGateway.NETWORK_ID))
                    floating_network = self.properties[self.FLOATING_NETWORK]
                except (ValueError, TypeError):
                    # Properties errors will be caught later in validation,
                    # where we can report them in their proper context.
                    continue
                if gateway_network == floating_network:
                    deps += (self, resource)

            # depend on any RouterInterface in this template which interfaces
            # with the same subnet that this floating IP's port is assigned
            # to
            elif resource.has_interface('OS::Neutron::RouterInterface'):
                self._add_router_interface_dependencies(deps, resource)
            # depend on Router with EXTERNAL_GATEWAY_NETWORK property
            # this template with the same network_id as this
            # floating_network_id
            elif resource.has_interface('OS::Neutron::Router'):
                try:
                    gateway = resource.properties.get(
                        router.Router.EXTERNAL_GATEWAY)
                    floating_network = self.properties[self.FLOATING_NETWORK]
                except (ValueError, TypeError):
                    # Properties errors will be caught later in validation,
                    # where we can report them in their proper context.
                    continue
                if gateway:
                    gateway_network = gateway.get(
                        router.Router.EXTERNAL_GATEWAY_NETWORK)
                    if gateway_network == floating_network:
                        deps += (self, resource)

    def validate(self):
        super(FloatingIP, self).validate()
        # fixed_ip_address cannot be specified without a port_id
        if self.properties[self.PORT_ID] is None and self.properties[
                self.FIXED_IP_ADDRESS] is not None:
            raise exception.ResourcePropertyDependency(
                prop1=self.FIXED_IP_ADDRESS, prop2=self.PORT_ID)

    def handle_create(self):
        props = self.prepare_properties(
            self.properties,
            self.physical_resource_name())
        props['floating_network_id'] = props.pop(self.FLOATING_NETWORK)
        if self.FLOATING_SUBNET in props:
            props['subnet_id'] = props.pop(self.FLOATING_SUBNET)
        fip = self.client().create_floatingip({
            'floatingip': props})['floatingip']
        self.resource_id_set(fip['id'])

    def handle_delete(self):
        with self.client_plugin().ignore_not_found:
            self.client().delete_floatingip(self.resource_id)
            return True

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        if prop_diff:
            port_id = prop_diff.get(self.PORT_ID,
                                    self.properties[self.PORT_ID])

            fixed_ip_address = prop_diff.get(
                self.FIXED_IP_ADDRESS,
                self.properties[self.FIXED_IP_ADDRESS])

            request_body = {
                'floatingip': {
                    'port_id': port_id,
                    'fixed_ip_address': fixed_ip_address}}

            self.client().update_floatingip(self.resource_id, request_body)


class FloatingIPAssociation(neutron.NeutronResource):
    """A resource for associating floating ips and ports.

    This resource allows associating a floating IP to a port with at least one
    IP address to associate with this floating IP.
    """
    PROPERTIES = (
        FLOATINGIP_ID, PORT_ID, FIXED_IP_ADDRESS,
    ) = (
        'floatingip_id', 'port_id', 'fixed_ip_address',
    )

    properties_schema = {
        FLOATINGIP_ID: properties.Schema(
            properties.Schema.STRING,
            _('ID of the floating IP to associate.'),
            required=True,
            update_allowed=True
        ),
        PORT_ID: properties.Schema(
            properties.Schema.STRING,
            _('ID of an existing port with at least one IP address to '
              'associate with this floating IP.'),
            required=True,
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('neutron.port')
            ]
        ),
        FIXED_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('IP address to use if the port has multiple addresses.'),
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('ip_addr')
            ]
        ),
    }

    def add_dependencies(self, deps):
        super(FloatingIPAssociation, self).add_dependencies(deps)

        for resource in self.stack.values():
            if resource.has_interface('OS::Neutron::RouterInterface'):

                def port_on_subnet(resource, subnet):
                    if not resource.has_interface('OS::Neutron::Port'):
                        return False
                    fixed_ips = resource.properties.get(
                        port.Port.FIXED_IPS) or []
                    for fixed_ip in fixed_ips:
                        port_subnet = (
                            fixed_ip.get(port.Port.FIXED_IP_SUBNET)
                            or fixed_ip.get(port.Port.FIXED_IP_SUBNET_ID))
                        return subnet == port_subnet
                    return False

                interface_subnet = (
                    resource.properties.get(router.RouterInterface.SUBNET) or
                    resource.properties.get(router.RouterInterface.SUBNET_ID))
                for d in deps.graph()[self]:
                    if port_on_subnet(d, interface_subnet):
                        deps += (self, resource)
                        break

    def handle_create(self):
        props = self.prepare_properties(self.properties, self.name)
        floatingip_id = props.pop(self.FLOATINGIP_ID)
        self.client().update_floatingip(floatingip_id, {
            'floatingip': props})
        self.resource_id_set(self.id)

    def handle_delete(self):
        if not self.resource_id:
            return

        with self.client_plugin().ignore_not_found:
            self.client().update_floatingip(
                self.properties[self.FLOATINGIP_ID],
                {'floatingip': {'port_id': None}})

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        if prop_diff:
            floatingip_id = self.properties[self.FLOATINGIP_ID]
            port_id = self.properties[self.PORT_ID]
            # if the floatingip_id is changed, disassociate the port which
            # associated with the old floatingip_id
            if self.FLOATINGIP_ID in prop_diff:
                with self.client_plugin().ignore_not_found:
                    self.client().update_floatingip(
                        floatingip_id,
                        {'floatingip': {'port_id': None}})

            # associate the floatingip with the new port
            floatingip_id = (prop_diff.get(self.FLOATINGIP_ID) or
                             floatingip_id)
            port_id = prop_diff.get(self.PORT_ID) or port_id

            fixed_ip_address = (prop_diff.get(self.FIXED_IP_ADDRESS) or
                                self.properties[self.FIXED_IP_ADDRESS])

            request_body = {
                'floatingip': {
                    'port_id': port_id,
                    'fixed_ip_address': fixed_ip_address}}

            self.client().update_floatingip(floatingip_id, request_body)
            self.resource_id_set(self.id)


class FloatingIPPortForward(neutron.NeutronResource):
    """A resource for creating port forwarding for floating IPs.

    This resource creates port forwarding for floating IPs.
    These are sub-resource of exsisting Floating ips, which requires the
    service_plugin and extension port_forwarding enabled and that the floating
    ip is not associated with a neutron port.
    """

    default_client_name = 'openstack'

    required_service_extension = 'floating-ip-port-forwarding'

    support_status = support.SupportStatus(
        status=support.SUPPORTED,
        version='19.0.0',
    )

    PROPERTIES = (
        INTERNAL_IP_ADDRESS, INTERNAL_PORT_NUMBER, EXTERNAL_PORT,
        INTERNAL_PORT, PROTOCOL, FLOATINGIP
    ) = (
        'internal_ip_address', 'internal_port_number',
        'external_port', 'internal_port', 'protocol', 'floating_ip'
    )

    properties_schema = {
        INTERNAL_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('Internal IP address to port forwarded to.'),
            required=True,
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('ip_addr')
            ]
        ),
        INTERNAL_PORT_NUMBER: properties.Schema(
            properties.Schema.INTEGER,
            _('Internal port number to port forward to.'),
            update_allowed=True,
            constraints=[
                constraints.Range(min=1, max=65535)
            ]
        ),
        EXTERNAL_PORT: properties.Schema(
            properties.Schema.INTEGER,
            _('External port address to port forward from.'),
            required=True,
            update_allowed=True,
            constraints=[
                constraints.Range(min=1, max=65535)
            ]
        ),
        INTERNAL_PORT: properties.Schema(
            properties.Schema.STRING,
            _('Name or ID of the internal_ip_address port.'),
            required=True,
            update_allowed=True,
            constraints=[
                constraints.CustomConstraint('neutron.port')
            ]
        ),
        PROTOCOL: properties.Schema(
            properties.Schema.STRING,
            _('Port protocol to forward.'),
            required=True,
            update_allowed=True,
            constraints=[
                constraints.AllowedValues([
                    'tcp', 'udp', 'icmp', 'icmp6', 'sctp', 'dccp'])
            ]
        ),
        FLOATINGIP: properties.Schema(
            properties.Schema.STRING,
            _('Name or ID of the floating IP create port forwarding on.'),
            required=True,
        ),
    }

    def translation_rules(self, props):
        client_plugin = self.client_plugin()
        return [
            translation.TranslationRule(
                props,
                translation.TranslationRule.RESOLVE,
                [self.FLOATINGIP],
                client_plugin=client_plugin,
                finder='find_network_ip'
            ),
            translation.TranslationRule(
                props,
                translation.TranslationRule.RESOLVE,
                [self.INTERNAL_PORT],
                client_plugin=client_plugin,
                finder='find_network_port'
            )
        ]

    def add_dependencies(self, deps):
        super(FloatingIPPortForward, self).add_dependencies(deps)

        for resource in self.stack.values():
            if resource.has_interface('OS::Neutron::RouterInterface'):

                def port_on_subnet(resource, subnet):
                    if not resource.has_interface('OS::Neutron::Port'):
                        return False
                    fixed_ips = resource.properties.get(
                        port.Port.FIXED_IPS) or []
                    for fixed_ip in fixed_ips:
                        port_subnet = (
                            fixed_ip.get(port.Port.FIXED_IP_SUBNET)
                            or fixed_ip.get(port.Port.FIXED_IP_SUBNET_ID))
                        return subnet == port_subnet
                    return False

                interface_subnet = (
                    resource.properties.get(router.RouterInterface.SUBNET) or
                    resource.properties.get(router.RouterInterface.SUBNET_ID))
                for d in deps.graph()[self]:
                    if port_on_subnet(d, interface_subnet):
                        deps += (self, resource)
                        break

    def handle_create(self):
        props = self.prepare_properties(self.properties, self.name)
        props['internal_port_id'] = props.pop(self.INTERNAL_PORT)
        props['internal_port'] = props.pop(self.INTERNAL_PORT_NUMBER)
        fp = self.client().network.create_floating_ip_port_forwarding(
            props.pop(self.FLOATINGIP),
            **props)
        self.resource_id_set(fp.id)

    def handle_delete(self):
        if not self.resource_id:
            return

        self.client().network.delete_floating_ip_port_forwarding(
            self.properties[self.FLOATINGIP],
            self.resource_id,
            ignore_missing=True
            )

    def handle_check(self):
        self.client().network.get_port_forwarding(
            self.resource_id,
            self.properties[self.FLOATINGIP]
        )

    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        if prop_diff:
            # Create a new dictionary to store the corrected properties
            updated_props = {}
            for key, value in prop_diff.items():
                if key == self.INTERNAL_PORT_NUMBER:
                    # Replace internal_port_number with internal_port
                    updated_props['internal_port'] = value
                elif key == self.INTERNAL_PORT:
                    # Replace internal_port with internal_port_id
                    updated_props['internal_port_id'] = value
                else:
                    updated_props[key] = value
            self.client().network.update_floating_ip_port_forwarding(
                self.properties[self.FLOATINGIP],
                self.resource_id,
                **updated_props)


def resource_mapping():
    return {
        'OS::Neutron::FloatingIP': FloatingIP,
        'OS::Neutron::FloatingIPAssociation': FloatingIPAssociation,
        'OS::Neutron::FloatingIPPortForward': FloatingIPPortForward,
    }
