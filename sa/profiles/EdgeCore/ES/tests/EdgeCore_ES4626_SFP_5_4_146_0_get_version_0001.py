# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_version test
## Auto-generated by ./noc debug-script at 18.05.2012 16:47:58
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class EdgeCore_ES_get_version_Test(ScriptTestCase):
    script = "EdgeCore.ES.get_version"
    vendor = "EdgeCore"
    platform = "ES4626-SFP"
    version = "5.4.146.0"
    input = {}
    result = {'attributes': {'Boot PROM': '1.6.5', 'HW version': '3.0'},
 'platform': 'ES4626-SFP',
 'vendor': 'EdgeCore',
 'version': '5.4.146.0'}
    motd = '********\n'
    cli = {
## 'show version 1'
'show version 1': """show version 1
  ES4626-SFP Device, Compiled Jan 15 18:30:40 2009
  SoftWare Package Version ES4626-SFP_5.4.146.0
  BootRom Version ES4626-SFP_1.6.5
  HardWare Version 3.0
  Copyright (C) 2001-2007 by Accton Technology Corp.
  All rights reserved.
  Last reboot is cold reset.
  Uptime is 24 weeks, 0 days, 4 hours, 21 minutes.""", 
'show system':  "show system\n                     ^\n% Invalid input detected at '^' marker.\n", 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
