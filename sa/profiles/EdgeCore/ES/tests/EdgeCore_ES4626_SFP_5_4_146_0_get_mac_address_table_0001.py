# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES4626.get_mac_address_table test
## Auto-generated by manage.py debug-script at 2010-11-26 14:50:03
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class EdgeCore_ES4626_get_mac_address_table_Test(ScriptTestCase):
    script="EdgeCore.ES.get_mac_address_table"
    vendor="EdgeCore"
    platform='ES4626-SFP'
    version='5.4.146.0'
    input={}
    result=[{'interfaces': ['Ethernet1/14'],
      'mac': '00:0E:2E:56:52:D7',
      'type': 'D',
      'vlan_id': 10},
     {'interfaces': ['Ethernet1/14'],
      'mac': '00:11:6B:91:F0:C5',
      'type': 'D',
      'vlan_id': 10},
     {'interfaces': ['CPU'],
      'mac': '00:12:CF:82:08:DC',
      'type': 'S',
      'vlan_id': 10},
     {'interfaces': ['Ethernet1/14'],
      'mac': '00:15:58:15:6D:EC',
      'type': 'D',
      'vlan_id': 10},
     {'interfaces': ['Ethernet1/14'],
      'mac': '4C:00:10:54:DA:39',
      'type': 'D',
      'vlan_id': 10},
     {'interfaces': ['Ethernet1/14'],
      'mac': '6C:F0:49:01:9F:93',
      'type': 'D',
      'vlan_id': 10},
     {'interfaces': ['Ethernet1/14'],
      'mac': 'E0:CB:4E:E7:D0:9D',
      'type': 'D',
      'vlan_id': 10},
     {'interfaces': ['Ethernet1/3'],
      'mac': '00:01:6C:B5:1D:61',
      'type': 'D',
      'vlan_id': 11},
     {'interfaces': ['Ethernet1/20'],
      'mac': '00:04:AC:A3:8E:1D',
      'type': 'D',
      'vlan_id': 11},
     {'interfaces': ['Ethernet1/15'],
      'mac': '00:0F:B0:93:E6:7F',
      'type': 'D',
      'vlan_id': 11},
     {'interfaces': ['Ethernet1/3'],
      'mac': '00:11:D8:7D:C8:50',
      'type': 'D',
      'vlan_id': 11},
     {'interfaces': ['CPU'],
      'mac': '00:12:CF:82:08:DC',
      'type': 'S',
      'vlan_id': 11},
     {'interfaces': ['Ethernet1/3'],
      'mac': '00:13:46:61:D7:5E',
      'type': 'D',
      'vlan_id': 11},
     {'interfaces': ['Ethernet1/20'],
      'mac': '00:15:F2:A7:53:AE',
      'type': 'D',
      'vlan_id': 11},
     {'interfaces': ['Ethernet1/18'],
      'mac': '00:E0:4C:77:03:DD',
      'type': 'D',
      'vlan_id': 1036},
     {'interfaces': ['(discard)'],
      'mac': '00:E0:4C:CC:E6:8D',
      'type': 'S',
      'vlan_id': 1036},
     {'interfaces': ['Ethernet1/18'],
      'mac': '00:E0:4D:1B:C0:6F',
      'type': 'D',
      'vlan_id': 1036},
     {'interfaces': ['Ethernet1/24'],
      'mac': '00:26:88:70:7F:0E',
      'type': 'D',
      'vlan_id': 4024}]
    motd='********\n'
    cli={
## 'show mac-address-table'
'show mac-address-table': """show mac-address-table
Read mac address table....
Vlan Mac Address                 Type    Creator   Ports
---- --------------------------- ------- -------------------------------------
10   00-0e-2e-56-52-d7           DYNAMIC Hardware Ethernet1/14
10   00-11-6b-91-f0-c5           DYNAMIC Hardware Ethernet1/14
10   00-12-cf-82-08-dc           STATIC  System   CPU
10   00-15-58-15-6d-ec           DYNAMIC Hardware Ethernet1/14
10   4c-00-10-54-da-39           DYNAMIC Hardware Ethernet1/14
10   6c-f0-49-01-9f-93           DYNAMIC Hardware Ethernet1/14
10   e0-cb-4e-e7-d0-9d           DYNAMIC Hardware Ethernet1/14
11   00-01-6c-b5-1d-61           DYNAMIC Hardware Ethernet1/3
11   00-04-ac-a3-8e-1d           DYNAMIC Hardware Ethernet1/20
11   00-0f-b0-93-e6-7f           DYNAMIC Hardware Ethernet1/15
11   00-11-d8-7d-c8-50           DYNAMIC Hardware Ethernet1/3
11   00-12-cf-82-08-dc           STATIC  System   CPU
11   00-13-46-61-d7-5e           DYNAMIC Hardware Ethernet1/3
11   00-15-f2-a7-53-ae           DYNAMIC Hardware Ethernet1/20
1036 00-e0-4c-77-03-dd           DYNAMIC Hardware Ethernet1/18
1036 00-e0-4c-cc-e6-8d           STATIC  User     (discard)
1036 00-e0-4d-1b-c0-6f           DYNAMIC Hardware Ethernet1/18
4024 00-26-88-70-7f-0e           DYNAMIC Hardware Ethernet1/24""",
}
    snmp_get={}
    snmp_getnext={}
