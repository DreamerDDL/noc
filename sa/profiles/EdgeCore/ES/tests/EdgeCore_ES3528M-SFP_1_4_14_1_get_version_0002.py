# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_version test
## Auto-generated by ./noc debug-script at 2012-02-23 21:48:59
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class EdgeCore_ES_get_version_Test(ScriptTestCase):
    script = "EdgeCore.ES.get_version"
    vendor = "EdgeCore"
    platform = 'ES3528M-SFP'
    version = '1.4.14.1'
    input = {}
    result = {'attributes': {'HW version': 'R01A', 'Serial Number': '053001153'},
 'platform': 'ES3528M',
 'vendor': 'EdgeCore',
 'version': '1.4.14.1'}
    motd = ' \n\n      CLI session with the ES3528M-SFP is opened.\n      To end the CLI session, enter [Exit].\n\nNo configured settings for reloading.\n'
    cli = {
## 'show version'
'show version': """show version
Unit 1
 Serial Number:           053001153
 Hardware Version:        R01A
 Chip Device ID:          Marvell 98DX106-B0, 88E6095[F]
 EPLD Version:            1.03
 Number of Ports:         28
 Main Power Status:       Up
 Redundant Power Status:  Not present

Agent (Master)
 Unit ID:                 1
 Loader Version:          1.0.1.0
 Boot ROM Version:        1.2.1.0
 Operation Code Version:  1.4.14.1""",
'terminal length 0':  'terminal length 0\n',
## 'show system'
'show system': """show system
System Description: ES3528M-SFP
System OID String: 1.3.6.1.4.1.259.8.2.4
System Information
 System Up Time:          84 days, 4 hours, 29 minutes, and 47.79 seconds
 System Name:             sw-ud148-opt/2
 System Location:         [NONE]
 System Contact:          [NONE]
 MAC Address (Unit1):     70-72-CF-2E-87-E8
 Web Server:              Disabled
 Web Server Port:         80
 Web Secure Server:       Disabled
 Web Secure Server Port:  443
 Telnet Server:           Enabled
 Telnet Server Port:      23
 Jumbo Frame:             Disabled """,
}
    snmp_get = {'1.3.6.1.2.1.1.1.0': 'ES3528M-SFP',
 '1.3.6.1.2.1.1.2.0': '1.3.6.1.4.1.259.8.2.4',
 '1.3.6.1.4.1.259.8.1.4.1.1.3.1.6.1': '1.4.14.1'}
    snmp_getnext = {}
    http_get = {}
