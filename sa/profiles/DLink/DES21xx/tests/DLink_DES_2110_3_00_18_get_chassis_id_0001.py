# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## DLink.DES21xx.get_chassis_id test
## Auto-generated by ./noc debug-script at 2011-12-16 11:05:24
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class DLink_DES21xx_get_chassis_id_Test(ScriptTestCase):
    script = "DLink.DES21xx.get_chassis_id"
    vendor = "DLink"
    platform = 'DES-2110'
    version = '3.00.18'
    input = {}
    result = '00:13:46:2D:C6:2D'
    motd = ''
    cli = {
## 'show switch'
'show switch': """show switch
Command:  show switch

Product Name:DES-2110                               
Firmware Version:3.00.18
Protocol Version:2.001.002
DHCP:Disable
IP Address:10.90.91.103
Subnet mask:255.255.255.0
Default gateway:10.90.91.1
Trap IP:10.90.0.12
MAC address:00-13-46-2d-c6-2d
System Name:p1a-sw1
Location Name:p1a-sw1
System Contact:
System Aging Time:300
VLAN Type:802.1Q BASE
Login Timeout (minutes):5
System UpTime:27 days 15 hours 20 mins 36 seconds
Web Server Port:80
""", 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
