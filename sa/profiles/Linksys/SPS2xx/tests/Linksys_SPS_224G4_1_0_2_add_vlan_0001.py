# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Linksys.SPS2xx.add_vlan test
## Auto-generated by ./noc debug-script at 2012-02-16 14:15:26
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Linksys_SPS2xx_add_vlan_Test(ScriptTestCase):
    script = "Linksys.SPS2xx.add_vlan"
    vendor = "Linksys"
    platform = 'SPS-224G4'
    version = '1.0.2'
    input = {'name': 'Test', 'tagged_ports': ['e18', 'g3', 'g4'], 'vlan_id': 777}
    result = True
    motd = ''
    cli = {
'':  '\n', 
'copy running-config startup-config':  'copy running-config startup-config\nCopy succeeded\n', 
'end':  'end\n', 
'configure':  'configure\n', 
## 'show vlan'
'show vlan': """show vlan

Vlan       Name                   Ports                Type     Authorization 
---- ----------------- --------------------------- ------------ ------------- 
 1           1               g(3-4),ch(1-8)           other       Required    
 72   area_SmileLink         e(2-24),g(1-4)         permanent     Required    
111     commutators              g(3-4)             permanent     Required    
140  Bankomats_clients          e1,g(3-4)           permanent     Required    
""", 
'vlan 777':  'vlan 777\n', 
'vlan database':  'vlan database\n', 
'name Test':  'name Test\n', 
'terminal datadump':  'terminal datadump\n', 
'exit':  'exit\n', 
'interface range ethernet e18,g3,g4':  'interface range ethernet e18,g3,g4\n', 
'interface vlan 777':  'interface vlan 777\n', 
'switchport trunk allowed vlan add  777':  'switchport trunk allowed vlan add  777\n', 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
