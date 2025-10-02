# Copyright 2023 Red Hat, Inc.
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

from unittest import mock

from oslo_config import cfg

from ovn_bgp_agent import constants
from ovn_bgp_agent.drivers.openstack.utils import evpn as evpn_utils
from ovn_bgp_agent.drivers.openstack.utils import ovn as ovn_utils
from ovn_bgp_agent.drivers.openstack.utils import ovs as ovs_utils
from ovn_bgp_agent.drivers.openstack.utils import wire
from ovn_bgp_agent import exceptions as agent_exc
from ovn_bgp_agent.tests import base as test_base
from ovn_bgp_agent.tests import utils as test_utils
from ovn_bgp_agent.utils import linux_net

CONF = cfg.CONF


class TestWire(test_base.TestCase):

    def setUp(self):
        super(TestWire, self).setUp()
        self.nb_idl = ovn_utils.OvsdbNbOvnIdl(mock.Mock())
        self.sb_idl = ovn_utils.OvsdbSbOvnIdl(mock.Mock())
        self.ovs_idl = mock.Mock()

        # Helper variables that are used across multiple methods
        self.bridge_mappings = ['datacentre:br-ex']

        self.ovs_idl.get_ovn_bridge_mappings.return_value = (
            self.bridge_mappings)

        # Monkey-patch parent class methods
        self.nb_idl.ls_add = mock.Mock()
        self.nb_idl.lr_add = mock.Mock()
        self.nb_idl.lrp_add = mock.Mock()
        self.nb_idl.lrp_set_gateway_chassis = mock.Mock()
        self.nb_idl.lrp_add_networks = mock.Mock()
        self.nb_idl.lr_route_add = mock.Mock()
        self.nb_idl.lr_policy_add = mock.Mock()

    @mock.patch.object(wire, '_ensure_base_wiring_config_underlay')
    def test_ensure_base_wiring_config(self, mock_underlay):
        wire.ensure_base_wiring_config(self.sb_idl, self.ovs_idl,
                                       routing_tables={})
        mock_underlay.assert_called_once_with(self.sb_idl, self.ovs_idl, {})

    @mock.patch.object(wire, '_ensure_base_wiring_config_ovn')
    def test_ensure_base_wiring_config_ovn(self, mock_ovn):
        CONF.set_override('exposing_method', 'ovn')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        wire.ensure_base_wiring_config(self.sb_idl, self.ovs_idl,
                                       ovn_idl=self.nb_idl)
        mock_ovn.assert_called_once_with(self.ovs_idl, self.nb_idl)

    @mock.patch.object(wire, '_ensure_base_wiring_config_evpn')
    def test_ensure_base_wiring_config_evpn(self, mock_evpn):
        CONF.set_override('exposing_method', 'vrf')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        wire.ensure_base_wiring_config(self.nb_idl, self.ovs_idl,
                                       ovn_idl=self.nb_idl)
        mock_evpn.assert_called_once_with(self.nb_idl, self.ovs_idl)

    @mock.patch.object(wire, '_ensure_base_wiring_config_underlay')
    @mock.patch.object(wire, '_ensure_base_wiring_config_ovn')
    def test_ensure_base_wiring_config_not_implemented(self, mock_ovn,
                                                       mock_underlay):
        CONF.set_override('exposing_method', 'dynamic')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        self.assertRaises(agent_exc.UnsupportedWiringConfig,
                          wire.ensure_base_wiring_config,
                          self.sb_idl, self.ovs_idl, ovn_idl=self.nb_idl)
        mock_ovn.assert_not_called()
        mock_underlay.assert_not_called()

    def test__ensure_base_wiring_config_ovn(self):
        pass

    @mock.patch.object(linux_net, 'get_interface_address')
    @mock.patch.object(ovs_utils, 'get_ovs_patch_ports_info')
    def test__ensure_base_wiring_config_evpn(self, m_get_ovs_patch_ports_info,
                                             m_get_interface_address):
        localnet_ports = [test_utils.create_row(
            tag=[4096],
        )]
        ports = localnet_ports + [test_utils.create_row(
            dhcpv4_options=[test_utils.create_row()],
            dhcpv6_options=[],
        )]
        get_localnet_ports_by_network_name = mock.patch.object(
            self.nb_idl, 'get_localnet_ports_by_network_name').start()
        get_localnet_ports_by_network_name.return_value = localnet_ports

        provnets = [test_utils.create_row(
            name='fake-provnet',
            external_ids={
                constants.OVN_EVPN_VNI_EXT_ID_KEY: 100,
            },
            ports=ports,
        )]
        get_bgpvpn_networks_for_ports = mock.patch.object(
            self.nb_idl, 'get_bgpvpn_networks_for_ports').start()
        get_bgpvpn_networks_for_ports.return_value = provnets

        CONF.set_override('evpn_local_ip', '127.0.0.1')
        self.addCleanup(CONF.clear_override, 'evpn_local_ip')

        vlan_dev = mock.MagicMock()

        evpn_bridge = mock.MagicMock()
        evpn_bridge.connect_vlan.return_value = vlan_dev

        evpn_setup = mock.patch.object(evpn_utils, 'setup').start()
        evpn_setup.return_value = evpn_bridge

        wire._ensure_base_wiring_config_evpn(self.nb_idl, self.ovs_idl)

        evpn_setup.assert_called_with(ovs_bridge='br-ex',
                                      vni=100,
                                      evpn_opts={'route_targets': [],
                                                 'route_distinguishers': [],
                                                 'export_targets': [],
                                                 'import_targets': []},
                                      mode=constants.OVN_EVPN_TYPE_L3,
                                      ovs_flows=mock.ANY)

        evpn_bridge.connect_vlan.assert_called_with(ports[0])
        vlan_dev.process_dhcp_opts.assert_called()

    def test__ensure_ovn_router(self):
        wire._ensure_ovn_router(self.nb_idl)
        self.nb_idl.lr_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, may_exist=True)

    @mock.patch.object(wire, '_execute_commands')
    @mock.patch.object(wire, '_ensure_lsp_cmds')
    def test__ensure_ovn_switch(self, m_ensure_lsp, m_cmds):
        ls_name = 'test-ls'
        localnet_port = "{}-localnet".format(ls_name)
        options = {'network_name': ls_name}

        wire._ensure_ovn_switch(self.nb_idl, ls_name)
        self.nb_idl.ls_add.assert_called_once_with(ls_name, may_exist=True)
        m_ensure_lsp.assert_called_once_with(
            self.nb_idl, localnet_port, ls_name, 'localnet', 'unknown',
            **options)

    @mock.patch.object(wire, '_execute_commands')
    @mock.patch.object(wire, '_ensure_lsp_cmds')
    def test__ensure_ovn_network_link_internal(self, m_ensure_lsp, m_cmds):
        switch_name = 'internal'
        provider_cidrs = ['172.16.0.0/16']
        r_port_name = "{}-openstack".format(constants.OVN_CLUSTER_ROUTER)
        options = {'router-port': r_port_name, 'arp_proxy': '172.16.0.0/16'}

        wire._ensure_ovn_network_link_internal(
            self.nb_idl, switch_name, provider_cidrs)

        self.nb_idl.lrp_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, r_port_name,
            constants.OVN_CLUSTER_ROUTER_INTERNAL_MAC, provider_cidrs, peer=[],
            may_exist=True)
        m_ensure_lsp.assert_called_once_with(
            self.nb_idl, mock.ANY, switch_name, 'router', 'router', **options)
        self.nb_idl.lrp_set_gateway_chassis.assert_called_once_with(
            r_port_name, CONF.local_ovn_cluster.bgp_chassis_id, 1)

    @mock.patch.object(wire, '_execute_commands')
    @mock.patch.object(wire, '_ensure_lsp_cmds')
    def test__ensure_ovn_network_link_internal_multiple_cidrs(self,
                                                              m_ensure_lsp,
                                                              m_cmds):
        switch_name = 'internal'
        provider_cidrs = ['172.16.0.0/16', '192.0.2.0/24']
        r_port_name = "{}-openstack".format(constants.OVN_CLUSTER_ROUTER)
        options = {'router-port': r_port_name,
                   'arp_proxy': '172.16.0.0/16 192.0.2.0/24'}

        wire._ensure_ovn_network_link_internal(
            self.nb_idl, switch_name, provider_cidrs)

        self.nb_idl.lrp_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, r_port_name,
            constants.OVN_CLUSTER_ROUTER_INTERNAL_MAC, provider_cidrs, peer=[],
            may_exist=True)
        m_ensure_lsp.assert_called_once_with(
            self.nb_idl, mock.ANY, switch_name, 'router', 'router', **options)
        self.nb_idl.lrp_set_gateway_chassis.assert_called_once_with(
            r_port_name, CONF.local_ovn_cluster.bgp_chassis_id, 1)

    @mock.patch.object(wire, '_execute_commands')
    @mock.patch.object(wire, '_ensure_lsp_cmds')
    def test__ensure_ovn_network_link_internal_runtime_error(
            self, m_ensure_lsp, m_cmds):
        switch_name = 'internal'
        provider_cidrs = ['172.16.0.0/16']
        r_port_name = "{}-openstack".format(constants.OVN_CLUSTER_ROUTER)
        options = {'router-port': r_port_name, 'arp_proxy': '172.16.0.0/16'}
        self.nb_idl.lrp_add.side_effect = RuntimeError(
            'with different networks')

        wire._ensure_ovn_network_link_internal(
            self.nb_idl, switch_name, provider_cidrs)

        self.nb_idl.lrp_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, r_port_name,
            constants.OVN_CLUSTER_ROUTER_INTERNAL_MAC, provider_cidrs, peer=[],
            may_exist=True)
        self.nb_idl.lrp_add_networks.assert_called_once_with(
            r_port_name, provider_cidrs, may_exist=True)
        m_ensure_lsp.assert_called_once_with(
            self.nb_idl, mock.ANY, switch_name, 'router', 'router', **options)
        self.nb_idl.lrp_set_gateway_chassis.assert_called_once_with(
            r_port_name, CONF.local_ovn_cluster.bgp_chassis_id, 1)

    @mock.patch.object(wire, '_execute_commands')
    @mock.patch.object(wire, '_ensure_lsp_cmds')
    def test__ensure_ovn_network_link_external(
            self, m_ensure_lsp, m_cmds):
        switch_name = 'external'
        ip = '1.1.1.2'
        mac = 'fake-map'
        r_port_name = "{}-{}".format(constants.OVN_CLUSTER_ROUTER, switch_name)
        options = {'router-port': r_port_name}

        wire._ensure_ovn_network_link_external(
            self.nb_idl, switch_name, ip, mac)

        self.nb_idl.lrp_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, r_port_name,
            mac, [ip], peer=[], may_exist=True)
        m_ensure_lsp.assert_called_once_with(
            self.nb_idl, mock.ANY, switch_name, 'router', 'router', **options)

    def _ensure_ovn_policies(self, next_hops):
        if len(next_hops) > 1:
            columns = {'nexthops': next_hops}
        elif len(next_hops) == 1:
            columns = {'nexthop': next_hops[0]}

        wire._ensure_ovn_policies(self.nb_idl, next_hops)

        self.nb_idl.lr_policy_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, 10, mock.ANY, 'reroute',
            may_exist=True, **columns)

    def test__ensure_ovn_policies_dual_nexthop(self):
        next_hops = ['1.1.1.1', '2.2.2.2']
        self._ensure_ovn_policies(next_hops)

    def test__ensure_ovn_policies_single_nexthop(self):
        next_hops = ['1.1.1.1']
        self._ensure_ovn_policies(next_hops)

    @mock.patch.object(wire, '_execute_commands')
    def test_ensure_ovn_routes(self, m_cmds):
        peer_ips = ['1.1.1.1']
        bfds = [test_utils.create_row(uuid='bfd')]
        wire._ensure_ovn_routes(self.nb_idl, peer_ips, bfds)
        self.nb_idl.lr_route_add.assert_called_once_with(
            constants.OVN_CLUSTER_ROUTER, '0.0.0.0/0', peer_ips[0],
            ecmp=True, may_exist=True, bfd=bfds[0].uuid)

    @mock.patch.object(ovs_utils, 'ensure_flow')
    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(ovs_utils, 'get_ovs_ports_info')
    @mock.patch.object(ovs_utils, 'get_ovs_patch_ports_info')
    def test__ensure_ingress_flows(self, m_ovs_patch, m_ovs_get, m_ip_version,
                                   m_ovn_flow):
        CONF.set_override('external_nics', ['eth1'], group='local_ovn_cluster')
        self.addCleanup(CONF.clear_override, 'external_nics',
                        group='local_ovn_cluster')
        bridge = 'br-ex'
        mac = 'fake-mac'
        switch_name = 'test-ls'
        provider_cidrs = ['172.16.0.0/16']
        patch_port_prefix = 'patch-{}-'.format(switch_name)
        m_ovs_patch.return_value = ['fake-patch']
        m_ovs_get.return_value = ['eth1']
        wire._ensure_ingress_flows(bridge, mac, switch_name, provider_cidrs)
        m_ovs_patch.assert_called_once_with(bridge, prefix=patch_port_prefix)
        m_ovs_get.assert_called_once_with(bridge)
        m_ip_version.assert_called_once_with(provider_cidrs[0])
        m_ovn_flow.assert_called_once_with(bridge, mock.ANY)

    @mock.patch.object(ovs_utils, 'get_ovs_patch_ports_info')
    def test__ensure_ingress_flows_no_network(self, m_ovs):
        bridge = 'br-ex'
        mac = 'fake-mac'
        switch_name = 'test-ls'
        provider_cidrs = []
        wire._ensure_ingress_flows(bridge, mac, switch_name, provider_cidrs)
        m_ovs.assert_not_called()

    @mock.patch.object(ovs_utils, 'get_ovs_ports_info')
    @mock.patch.object(ovs_utils, 'get_ovs_patch_ports_info')
    def test__ensure_ingress_flows_no_patch_port(self, m_ovs_patch, m_ovs_get):
        bridge = 'br-ex'
        mac = 'fake-mac'
        switch_name = 'test-ls'
        provider_cidrs = ['172.16.0.0/16']
        patch_port_prefix = 'patch-{}-'.format(switch_name)
        m_ovs_patch.return_value = []
        wire._ensure_ingress_flows(bridge, mac, switch_name, provider_cidrs)
        m_ovs_patch.assert_called_once_with(bridge, prefix=patch_port_prefix)
        m_ovs_get.assert_not_called()

    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(ovs_utils, 'get_ovs_ports_info')
    @mock.patch.object(ovs_utils, 'get_ovs_patch_ports_info')
    def test__ensure_ingress_flows_no_external_nic(self, m_ovs_patch,
                                                   m_ovs_get, m_ip_version):
        bridge = 'br-ex'
        mac = 'fake-mac'
        switch_name = 'test-ls'
        provider_cidrs = ['172.16.0.0/16']
        patch_port_prefix = 'patch-{}-'.format(switch_name)
        m_ovs_patch.return_value = ['fake-patch']
        m_ovs_get.return_value = ['eth1']
        wire._ensure_ingress_flows(bridge, mac, switch_name, provider_cidrs)
        m_ovs_patch.assert_called_once_with(bridge, prefix=patch_port_prefix)
        m_ovs_get.assert_called_once_with(bridge)
        m_ip_version.assert_not_called()

    @mock.patch.object(wire, '_cleanup_wiring_underlay')
    def test_cleanup_wiring_underlay(self, mock_underlay):
        ovs_flows = {}
        exposed_ips = {}
        routing_tables = {}
        routing_tables_routes = {}
        wire.cleanup_wiring(self.sb_idl, self.bridge_mappings, ovs_flows,
                            exposed_ips, routing_tables, routing_tables_routes)
        mock_underlay.assert_called_once_with(
            self.sb_idl, self.bridge_mappings, ovs_flows, exposed_ips,
            routing_tables, routing_tables_routes)

    @mock.patch.object(linux_net, 'get_exposed_ips')
    @mock.patch.object(linux_net, 'delete_exposed_ips')
    def test_cleanup_wiring_ovn(self, _delete_exposed_ips, _get_exposed_ips):
        CONF.set_override('exposing_method', 'ovn')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        # Both IPs are present on the NIC but .42 is not expected
        # to be exposed.
        _get_exposed_ips.return_value = ['192.0.2.42', '192.0.2.24']

        ovs_flows = {}
        exposed_ips = {
            "fakels": {"192.0.2.24": {'bridge_device': "br-example"}}}
        routing_tables = {}
        routing_tables_routes = {}
        wire.cleanup_wiring(self.sb_idl, self.bridge_mappings, ovs_flows,
                            exposed_ips, routing_tables,
                            routing_tables_routes)
        # Make sure we only delete the IP that isn't supposed to be exposed.
        _delete_exposed_ips.assert_called_once_with({"192.0.2.42"},
                                                    CONF.bgp_nic)

    def test_cleanup_wiring_evpn(self):
        CONF.set_override('exposing_method', 'vrf')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        vlan_dev = mock.MagicMock()
        evpn_bridge = mock.MagicMock()
        evpn_bridge.get_vlan.return_value = vlan_dev
        ovs_flows = {
            'foo': {
                'evpn': {
                    '4096': evpn_bridge,
                }
            }
        }
        exposed_ips = {}
        routing_tables = {}
        routing_tables_routes = {}
        ret = wire.cleanup_wiring(self.sb_idl, self.bridge_mappings, ovs_flows,
                                  exposed_ips, routing_tables,
                                  routing_tables_routes)

        evpn_bridge.get_vlan.assert_called_with('4096')
        vlan_dev.cleanup_excessive_routes.assert_called()
        self.assertTrue(ret)

    @mock.patch.object(wire, '_cleanup_wiring_underlay')
    def test_cleanup_wiring_not_implemeneted(self, mock_underlay):
        CONF.set_override('exposing_method', 'dynamic')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        ovs_flows = {}
        exposed_ips = {}
        routing_tables = {}
        routing_tables_routes = {}
        wire.cleanup_wiring(self.sb_idl, self.bridge_mappings, ovs_flows,
                            exposed_ips, routing_tables, routing_tables_routes)

        mock_underlay.assert_not_called()

    @mock.patch.object(wire, '_wire_provider_port_underlay')
    def test_wire_provider_port_underlay(self, mock_underlay):
        routing_tables_routes = {}
        ovs_flows = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        localnet = 'fake-localnet'
        routing_table = 5
        proxy_cidrs = []

        wire.wire_provider_port(routing_tables_routes, ovs_flows, port_ips,
                                bridge_device, bridge_vlan, localnet,
                                routing_table, proxy_cidrs)
        mock_underlay.assert_called_once_with(
            routing_tables_routes, ovs_flows, port_ips, bridge_device,
            bridge_vlan, localnet, routing_table, proxy_cidrs, lladdr=None)

    @mock.patch.object(wire, '_wire_provider_port_ovn')
    def test_wire_provider_port_ovn(self, mock_ovn):
        CONF.set_override('exposing_method', 'ovn')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        ovs_flows = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        localnet = 'fake-localnet'
        routing_table = 5
        proxy_cidrs = []
        mac = 'fake-mac'

        wire.wire_provider_port(routing_tables_routes, ovs_flows, port_ips,
                                bridge_device, bridge_vlan, localnet,
                                routing_table, proxy_cidrs, mac=mac,
                                ovn_idl=self.nb_idl)
        mock_ovn.assert_called_once_with(self.nb_idl, port_ips, mac)

    def test_wire_provider_port_evpn(self):
        CONF.set_override('exposing_method', 'vrf')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        ovs_flows = {}
        port_ips = ['10.10.10.1']
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        localnet = 'fake-localnet'
        routing_table = 5
        proxy_cidrs = []
        mac = 'fake-mac'

        vlan_dev = mock.MagicMock()

        evpn_bridge = mock.MagicMock()
        evpn_bridge.get_vlan.return_value = vlan_dev

        evpn_lookup = mock.patch.object(evpn_utils, 'lookup').start()
        evpn_lookup.return_value = evpn_bridge

        ret = wire.wire_provider_port(routing_tables_routes, ovs_flows,
                                      port_ips, bridge_device, bridge_vlan,
                                      localnet, routing_table, proxy_cidrs,
                                      mac=mac, ovn_idl=self.nb_idl)
        self.assertTrue(ret)

        evpn_lookup.assert_called_once_with(bridge_device, bridge_vlan)
        evpn_bridge.get_vlan.assert_called_once_with(bridge_vlan)
        vlan_dev.add_route.assert_called_with(routing_tables_routes,
                                              port_ips[0], mac, via=None)

    def test_wire_provider_port_evpn_unconfigured(self):
        CONF.set_override('exposing_method', 'vrf')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        ovs_flows = {}
        port_ips = ['10.10.10.1']
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        localnet = 'fake-localnet'
        routing_table = 5
        proxy_cidrs = []
        mac = 'fake-mac'

        evpn_lookup = mock.patch.object(evpn_utils, 'lookup').start()
        evpn_lookup.side_effect = KeyError

        ret = wire.wire_provider_port(routing_tables_routes, ovs_flows,
                                      port_ips, bridge_device, bridge_vlan,
                                      localnet, routing_table, proxy_cidrs,
                                      mac=mac, ovn_idl=self.nb_idl)
        self.assertIsNone(ret)

    @mock.patch.object(wire, '_wire_provider_port_underlay')
    @mock.patch.object(wire, '_wire_provider_port_ovn')
    @mock.patch.object(wire, '_wire_provider_port_evpn')
    def test_wire_provider_port_not_implemented(self, mock_evpn, mock_ovn,
                                                mock_underlay):
        CONF.set_override('exposing_method', 'dynamic')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        ovs_flows = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        localnet = 'fake-localnet'
        routing_table = 5
        proxy_cidrs = []

        wire.wire_provider_port(routing_tables_routes, ovs_flows, port_ips,
                                bridge_device, bridge_vlan, localnet,
                                routing_table, proxy_cidrs)

        mock_evpn.assert_not_called()
        mock_ovn.assert_not_called()
        mock_underlay.assert_not_called()

    @mock.patch.object(wire, '_execute_commands')
    def test__wire_provider_port_ovn(self, m_cmds):
        port_ips = ['1.1.1.1', '2.2.2.2']
        mac = 'fake-mac'
        port = "{}-openstack".format(constants.OVN_CLUSTER_ROUTER)

        wire._wire_provider_port_ovn(self.nb_idl, port_ips, mac)

        cmds = [
            ovn_utils.StaticMACBindingAddCommand(
                self.nb_idl, port, port_ips[0], mac, True, may_exist=True),
            ovn_utils.StaticMACBindingAddCommand(
                self.nb_idl, port, port_ips[1], mac, True, may_exist=True)]

        # FIXME(ltomasbo): The standard assert called ones is not working
        # with the object
        # m_cmds.assert_called_once_with(self.nb_idl, cmds)
        # so we are checking this by comparing the object dict instead
        self.assertEqual(
            m_cmds.call_args_list[0][0][1][0].__dict__,
            cmds[0].__dict__
        )

    @mock.patch.object(wire, '_execute_commands')
    def test__wire_provider_port_ovn_no_action(self, m_cmds):
        port_ips = []
        mac = 'fake-mac'
        wire._wire_provider_port_ovn(self.nb_idl, port_ips, mac)
        m_cmds.assert_not_called()

    @mock.patch.object(wire, '_unwire_provider_port_underlay')
    def test_unwire_provider_port_underlay(self, mock_underlay):
        routing_tables_routes = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_table = 5
        proxy_cidrs = []

        wire.unwire_provider_port(routing_tables_routes, port_ips,
                                  bridge_device, bridge_vlan, routing_table,
                                  proxy_cidrs)
        mock_underlay.assert_called_once_with(
            routing_tables_routes, port_ips, bridge_device, bridge_vlan,
            routing_table, proxy_cidrs, lladdr=None)

    @mock.patch.object(wire, '_unwire_provider_port_ovn')
    def test_unwire_provider_port_ovn(self, mock_ovn):
        CONF.set_override('exposing_method', 'ovn')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_table = 5
        proxy_cidrs = []

        wire.unwire_provider_port(routing_tables_routes, port_ips,
                                  bridge_device, bridge_vlan, routing_table,
                                  proxy_cidrs, ovn_idl=self.nb_idl)
        mock_ovn.assert_called_once_with(self.nb_idl, port_ips)

    @mock.patch.object(wire, '_unwire_provider_port_evpn')
    def test_unwire_provider_port_evpn(self, mock_evpn):
        CONF.set_override('exposing_method', 'vrf')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_table = 5
        proxy_cidrs = []

        wire.unwire_provider_port(routing_tables_routes, port_ips,
                                  bridge_device, bridge_vlan, routing_table,
                                  proxy_cidrs, mac='boo')
        mock_evpn.assert_called_once_with(routing_tables_routes, port_ips,
                                          bridge_device, bridge_vlan, 'boo')

    @mock.patch.object(wire, '_unwire_provider_port_underlay')
    @mock.patch.object(wire, '_unwire_provider_port_ovn')
    @mock.patch.object(wire, '_unwire_provider_port_evpn')
    def test_unwire_provider_port_not_implemented(self, mock_evpn, mock_ovn,
                                                  mock_underlay):
        CONF.set_override('exposing_method', 'dynamic')
        self.addCleanup(CONF.clear_override, 'exposing_method')

        routing_tables_routes = {}
        port_ips = []
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_table = 5
        proxy_cidrs = []

        wire.unwire_provider_port(routing_tables_routes, port_ips,
                                  bridge_device, bridge_vlan, routing_table,
                                  proxy_cidrs)
        mock_evpn.assert_not_called()
        mock_ovn.assert_not_called()
        mock_underlay.assert_not_called()

    def test__unwire_provider_port_evpn(self):
        routing_tables_routes = {}
        port_ips = ['10.10.10.1']
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        lladdr = 'boo'

        vlan_dev = mock.MagicMock()

        evpn_bridge = mock.MagicMock()
        evpn_bridge.get_vlan.return_value = vlan_dev

        evpn_lookup = mock.patch.object(evpn_utils, 'lookup').start()
        evpn_lookup.return_value = evpn_bridge

        ret = wire._unwire_provider_port_evpn(routing_tables_routes, port_ips,
                                              bridge_device, bridge_vlan,
                                              lladdr)
        self.assertTrue(ret)

        vlan_dev.del_route.assert_called_with(routing_tables_routes,
                                              port_ips[0], lladdr)

    def test__unwire_provider_port_evpn_unconfigured(self):
        routing_tables_routes = {}
        port_ips = ['10.10.10.1']
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        lladdr = 'boo'

        evpn_lookup = mock.patch.object(evpn_utils, 'lookup').start()
        evpn_lookup.side_effect = KeyError

        ret = wire._unwire_provider_port_evpn(routing_tables_routes, port_ips,
                                              bridge_device, bridge_vlan,
                                              lladdr)
        self.assertIsNone(ret)

    @mock.patch.object(wire, '_execute_commands')
    def test__unwire_provider_port_ovn(self, m_cmds):
        port_ips = ['1.1.1.1']
        port = "{}-openstack".format(constants.OVN_CLUSTER_ROUTER)

        wire._unwire_provider_port_ovn(self.nb_idl, port_ips)

        cmds = [ovn_utils.StaticMACBindingDelCommand(
                self.nb_idl, port, port_ips[0], if_exists=True)]

        # FIXME(ltomasbo): The standard assert called ones is not working
        # with the object
        # m_cmds.assert_called_once_with(self.nb_idl, cmds)
        # so we are checking this by comparing the object dict instead
        self.assertEqual(
            m_cmds.call_args_list[0][0][1][0].__dict__,
            cmds[0].__dict__
        )

    @mock.patch.object(wire, '_execute_commands')
    def test__unwire_provider_port_ovn_no_action(self, m_cmds):
        port_ips = []
        wire._unwire_provider_port_ovn(self.nb_idl, port_ips)
        m_cmds.assert_not_called()

    @mock.patch.object(wire, '_wire_lrp_port_underlay')
    def test_wire_lrp_port_underlay(self, mock_underlay):
        routing_tables_routes = {}
        ip = 'fake-ip'
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']

        wire.wire_lrp_port(routing_tables_routes, ip, bridge_device,
                           bridge_vlan, routing_tables, cr_lrp_ips)
        mock_underlay.assert_called_once_with(
            routing_tables_routes, ip, bridge_device, bridge_vlan,
            routing_tables, cr_lrp_ips)

    @mock.patch.object(wire, '_unwire_lrp_port_underlay')
    def test_unwire_lrp_port_underlay(self, mock_underlay):
        routing_tables_routes = {}
        ip = 'fake-ip'
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']

        wire.unwire_lrp_port(routing_tables_routes, ip, bridge_device,
                             bridge_vlan, routing_tables, cr_lrp_ips)
        mock_underlay.assert_called_once_with(
            routing_tables_routes, ip, bridge_device, bridge_vlan,
            routing_tables, cr_lrp_ips)

    @mock.patch.object(linux_net, 'add_ip_route')
    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(linux_net, 'add_ip_rule')
    def test__wire_lrp_port_underlay(self, m_ip_rule, m_ip_version,
                                     m_ip_route):
        routing_tables_routes = {}
        ip = '10.0.0.1/24'
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']

        ret = wire._wire_lrp_port_underlay(routing_tables_routes, ip,
                                           bridge_device, bridge_vlan,
                                           routing_tables, cr_lrp_ips)
        self.assertTrue(ret)
        m_ip_rule.assert_called_once_with(ip, 5)
        m_ip_route.assert_called_once_with(
            routing_tables_routes, '10.0.0.1', 5, 'fake-bridge',
            vlan='101', mask='24', via='fake-crlrp-ip')

    @mock.patch.object(linux_net, 'add_ip_rule')
    def test__wire_lrp_port_underlay_no_bridge(self, m_ip_rule):
        routing_tables_routes = {}
        ip = 'fake-ip'
        bridge_device = None
        bridge_vlan = None
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']

        ret = wire._wire_lrp_port_underlay(routing_tables_routes, ip,
                                           bridge_device, bridge_vlan,
                                           routing_tables, cr_lrp_ips)

        self.assertFalse(ret)
        m_ip_rule.assert_not_called()

    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(linux_net, 'add_ip_rule')
    def test__wire_lrp_port_underlay_invalid_ip(self, m_ip_rule, m_ip_version):
        routing_tables_routes = {}
        ip = 'fake-ip'
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']
        m_ip_rule.side_effect = agent_exc.InvalidPortIP(ip=ip)

        ret = wire._wire_lrp_port_underlay(routing_tables_routes, ip,
                                           bridge_device, bridge_vlan,
                                           routing_tables, cr_lrp_ips)

        self.assertFalse(ret)
        m_ip_rule.assert_called_once_with(ip, 5)
        m_ip_version.assert_not_called()

    @mock.patch.object(linux_net, 'add_ip_route')
    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(linux_net, 'add_ip_rule')
    def test__wire_lrp_port_underlay_advertisement_subnet(
        self, m_ip_rule, m_ip_version, m_ip_route):
        CONF.set_override(
            'advertisement_method_tenant_networks',
            constants.ADVERTISEMENT_METHOD_SUBNET)
        self.addCleanup(
            CONF.clear_override,
            'advertisement_method_tenant_networks')
        routing_tables_routes = {}
        ip = '10.0.0.1/24'
        bridge_device = 'fake-bridge'
        bridge_vlan = None
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']
        ret = wire._wire_lrp_port_underlay(
            routing_tables_routes, ip, bridge_device,
            bridge_vlan, routing_tables, cr_lrp_ips)
        self.assertTrue(ret)
        m_ip_rule.assert_called_once_with(ip, 5)
        expected_ip_route_calls = [
            mock.call(
                routing_tables_routes, ip.split('/')[0],
                routing_tables[bridge_device], bridge_device,
                vlan=bridge_vlan, mask=ip.split('/')[1], via=cr_lrp_ips[0]),
            mock.call(
                routing_tables_routes, ip.split('/')[0],
                CONF.bgp_vrf_table_id, CONF.bgp_nic,
                mask=ip.split('/')[1], via=cr_lrp_ips[0])]
        m_ip_route.assert_has_calls(expected_ip_route_calls)

    @mock.patch.object(linux_net, 'del_ip_route')
    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(linux_net, 'del_ip_rule')
    def test__unwire_lrp_port_underlay(self, m_ip_rule, m_ip_version,
                                       m_ip_route):
        routing_tables_routes = {}
        ip = '10.0.0.1/24'
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']

        ret = wire._unwire_lrp_port_underlay(routing_tables_routes, ip,
                                             bridge_device, bridge_vlan,
                                             routing_tables, cr_lrp_ips)
        self.assertTrue(ret)
        m_ip_rule.assert_called_once_with(ip, 5)
        m_ip_route.assert_called_once_with(
            routing_tables_routes, '10.0.0.1', 5, 'fake-bridge',
            vlan='101', mask='24', via='fake-crlrp-ip')

    @mock.patch.object(linux_net, 'del_ip_rule')
    def test__unwire_lrp_port_underlay_no_bridge(self, m_ip_rule):
        routing_tables_routes = {}
        ip = 'fake-ip'
        bridge_device = None
        bridge_vlan = None
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']

        ret = wire._unwire_lrp_port_underlay(routing_tables_routes, ip,
                                             bridge_device, bridge_vlan,
                                             routing_tables, cr_lrp_ips)

        self.assertFalse(ret)
        m_ip_rule.assert_not_called()

    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(linux_net, 'del_ip_rule')
    def test__unwire_lrp_port_underlay_invalid_ip(self, m_ip_rule,
                                                  m_ip_version):
        routing_tables_routes = {}
        ip = 'fake-ip'
        bridge_device = 'fake-bridge'
        bridge_vlan = '101'
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']
        m_ip_rule.side_effect = agent_exc.InvalidPortIP(ip=ip)

        ret = wire._unwire_lrp_port_underlay(routing_tables_routes, ip,
                                             bridge_device, bridge_vlan,
                                             routing_tables, cr_lrp_ips)

        self.assertFalse(ret)
        m_ip_rule.assert_called_once_with(ip, 5)
        m_ip_version.assert_not_called()

    @mock.patch.object(linux_net, 'del_ip_route')
    @mock.patch.object(linux_net, 'get_ip_version')
    @mock.patch.object(linux_net, 'del_ip_rule')
    def test__unwire_lrp_port_underlay_advertisement_subnet(
        self, m_ip_rule, m_ip_version, m_ip_route):
        CONF.set_override(
            'advertisement_method_tenant_networks',
            constants.ADVERTISEMENT_METHOD_SUBNET)
        self.addCleanup(
            CONF.clear_override,
            'advertisement_method_tenant_networks')
        routing_tables_routes = {}
        ip = '10.0.0.1/24'
        bridge_device = 'fake-bridge'
        bridge_vlan = None
        routing_tables = {'fake-bridge': 5}
        cr_lrp_ips = ['fake-crlrp-ip']
        ret = wire._unwire_lrp_port_underlay(
            routing_tables_routes, ip, bridge_device, bridge_vlan,
            routing_tables, cr_lrp_ips)
        self.assertTrue(ret)
        m_ip_rule.assert_called_once_with(ip, 5)
        expected_ip_route_calls = [
            mock.call(
                routing_tables_routes, ip.split('/')[0],
                routing_tables[bridge_device], bridge_device,
                vlan=bridge_vlan, mask=ip.split('/')[1], via=cr_lrp_ips[0]),
            mock.call(
                routing_tables_routes, ip.split('/')[0],
                CONF.bgp_vrf_table_id, CONF.bgp_nic,
                mask=ip.split('/')[1], via=cr_lrp_ips[0])]
        m_ip_route.assert_has_calls(expected_ip_route_calls)
