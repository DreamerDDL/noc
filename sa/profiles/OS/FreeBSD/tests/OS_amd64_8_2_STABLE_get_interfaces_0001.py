# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## OS.FreeBSD.get_interfaces test
## Auto-generated by ./noc debug-script at 21.09.2012 13:38:23
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class OS_FreeBSD_get_interfaces_Test(ScriptTestCase):
    script = "OS.FreeBSD.get_interfaces"
    vendor = "OS"
    platform = "amd64"
    version = "8.2-STABLE"
    input = {}
    result = [{'forwarding_instance': 'default',
  'interfaces': [{'admin_status': True,
                  'descriptions': 'Uplink',
                  'mac': '00:E0:81:40:8D:56',
                  'name': 'em0',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'descriptions': 'Uplink',
                                     'enabled_afi': ['IPv4'],
                                     'ipv4_addresses': ['10.111.0.14/24',
                                                        '192.168.1.1/24'],
                                     'is_ipv4': True,
                                     'mac': '00:E0:81:40:8D:56',
                                     'name': 'em0',
                                     'oper_status': True},
                                    {'admin_status': True,
                                     'enabled_afi': ['IPv4'],
                                     'ipv4_addresses': ['10.116.0.211/16'],
                                     'is_ipv4': True,
                                     'mac': '00:E0:81:40:8D:56',
                                     'name': 'em0.256',
                                     'oper_status': True,
                                     'vlan_ids': [256]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:E0:81:40:8D:57',
                  'name': 'em1',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['IPv6'],
                                     'ipv6_addresses': ['2001:db8:bdbd::123/48'],
                                     'is_ipv6': True,
                                     'mac': '00:E0:81:40:8D:57',
                                     'name': 'em1',
                                     'oper_status': False}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'name': 'lo0',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['IPv6', 'IPv4'],
                                     'ipv4_addresses': ['127.0.0.1/8'],
                                     'ipv6_addresses': ['::1/128'],
                                     'is_ipv4': True,
                                     'is_ipv6': True,
                                     'name': 'lo0',
                                     'oper_status': True}],
                  'type': 'loopback'}],
  'type': 'ip'}]
    motd = ''
    cli = {
## 'ifconfig -v'
'ifconfig -v': """ ifconfig -v
em0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
\tdescription: Uplink
\toptions=9b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM>
\tether 00:e0:81:40:8d:56
\tinet 10.111.0.14 netmask 0xffffff00 broadcast 10.111.0.255
\tinet 192.168.1.1 netmask 0xffffff00 broadcast 192.168.1.255
\tmedia: Ethernet autoselect (1000baseT <full-duplex>)
\tstatus: active
em1: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
\toptions=9b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM>
\tether 00:e0:81:40:8d:57
\tinet6 2001:db8:bdbd::123 prefixlen 48 
\tnd6 options=3<PERFORMNUD,ACCEPT_RTADV>
\tmedia: Ethernet autoselect
\tstatus: no carrier
ipfw0: flags=8801<UP,SIMPLEX,MULTICAST> metric 0 mtu 65536
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
\toptions=3<RXCSUM,TXCSUM>
\tinet6 fe80::1%lo0 prefixlen 64 scopeid 0x9 
\tinet6 ::1 prefixlen 128 
\tinet 127.0.0.1 netmask 0xff000000 
\tnd6 options=3<PERFORMNUD,ACCEPT_RTADV>
\tgroups: lo 
em0.256: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
\toptions=3<RXCSUM,TXCSUM>
\tether 00:e0:81:40:8d:56
\tinet 10.116.0.211 netmask 0xffff0000 broadcast 10.116.255.255
\tmedia: Ethernet autoselect (1000baseT <full-duplex>)
\tstatus: active
\tvlan: 256 parent interface: em0
\tgroups: vlan """, 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
