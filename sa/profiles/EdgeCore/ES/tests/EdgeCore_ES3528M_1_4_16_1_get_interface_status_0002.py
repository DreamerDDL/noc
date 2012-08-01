# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## EdgeCore.ES.get_interface_status test
## Auto-generated by ./noc debug-script at 01.08.2012 17:04:12
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class EdgeCore_ES_get_interface_status_Test(ScriptTestCase):
    script = "EdgeCore.ES.get_interface_status"
    vendor = "EdgeCore"
    platform = "Edge-Core FE L2 Switch ES3528M"
    version = "1.4.16.1"
    input = {}
    result = [{'description': 'ind40-1-riko.old.office',
  'interface': 'Eth 1/1',
  'mac': '70:72:CF:13:A1:41',
  'snmp_ifindex': 1,
  'status': True},
 {'description': 'eng126-riko.studio',
  'interface': 'Eth 1/2',
  'mac': '70:72:CF:13:A1:42',
  'snmp_ifindex': 2,
  'status': True},
 {'description': 'eng126-riko-loop',
  'interface': 'Eth 1/3',
  'mac': '70:72:CF:13:A1:43',
  'snmp_ifindex': 3,
  'status': True},
 {'description': 'kosyg/osip-Gldn',
  'interface': 'Eth 1/4',
  'mac': '70:72:CF:13:A1:44',
  'snmp_ifindex': 4,
  'status': False},
 {'description': 'koltush.loop',
  'interface': 'Eth 1/5',
  'mac': '70:72:CF:13:A1:45',
  'snmp_ifindex': 5,
  'status': True},
 {'description': 'koltush',
  'interface': 'Eth 1/6',
  'mac': '70:72:CF:13:A1:46',
  'snmp_ifindex': 6,
  'status': True},
 {'description': 'osupenko4.seg48',
  'interface': 'Eth 1/7',
  'mac': '70:72:CF:13:A1:47',
  'snmp_ifindex': 7,
  'status': True},
 {'description': '',
  'interface': 'Eth 1/8',
  'mac': '70:72:CF:13:A1:48',
  'snmp_ifindex': 8,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/9',
  'mac': '70:72:CF:13:A1:49',
  'snmp_ifindex': 9,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/10',
  'mac': '70:72:CF:13:A1:4A',
  'snmp_ifindex': 10,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/11',
  'mac': '70:72:CF:13:A1:4B',
  'snmp_ifindex': 11,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/12',
  'mac': '70:72:CF:13:A1:4C',
  'snmp_ifindex': 12,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/13',
  'mac': '70:72:CF:13:A1:4D',
  'snmp_ifindex': 13,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/14',
  'mac': '70:72:CF:13:A1:4E',
  'snmp_ifindex': 14,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/15',
  'mac': '70:72:CF:13:A1:4F',
  'snmp_ifindex': 15,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/16',
  'mac': '70:72:CF:13:A1:50',
  'snmp_ifindex': 16,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/17',
  'mac': '70:72:CF:13:A1:51',
  'snmp_ifindex': 17,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/18',
  'mac': '70:72:CF:13:A1:52',
  'snmp_ifindex': 18,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/19',
  'mac': '70:72:CF:13:A1:53',
  'snmp_ifindex': 19,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/20',
  'mac': '70:72:CF:13:A1:54',
  'snmp_ifindex': 20,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/21',
  'mac': '70:72:CF:13:A1:55',
  'snmp_ifindex': 21,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/22',
  'mac': '70:72:CF:13:A1:56',
  'snmp_ifindex': 22,
  'status': False},
 {'description': 'nastavn-36-2',
  'interface': 'Eth 1/23',
  'mac': '70:72:CF:13:A1:57',
  'snmp_ifindex': 23,
  'status': True},
 {'description': 'Kosygina-30-2',
  'interface': 'Eth 1/24',
  'mac': '70:72:CF:13:A1:58',
  'snmp_ifindex': 24,
  'status': True},
 {'description': '',
  'interface': 'Eth 1/25',
  'mac': '70:72:CF:13:A1:59',
  'snmp_ifindex': 25,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/26',
  'mac': '70:72:CF:13:A1:5A',
  'snmp_ifindex': 26,
  'status': False},
 {'description': '',
  'interface': 'Eth 1/27',
  'mac': '70:72:CF:13:A1:5B',
  'snmp_ifindex': 27,
  'status': True},
 {'description': 'uplink',
  'interface': 'Eth 1/28',
  'mac': '70:72:CF:13:A1:5C',
  'snmp_ifindex': 28,
  'status': True},
 {'description': '',
  'interface': 'VLAN 58',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 1058,
  'status': True},
 {'description': '',
  'interface': 'VLAN 52',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 1052,
  'status': True},
 {'description': '',
  'interface': 'VLAN 4000',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 5000,
  'status': True},
 {'description': '',
  'interface': 'Trunk 1',
  'mac': '70:72:CF:13:A1:52',
  'snmp_ifindex': 53,
  'status': False},
 {'description': '',
  'interface': 'VLAN 848',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 1848,
  'status': True},
 {'description': 'e38-eng126.riko',
  'interface': 'VLAN 3048',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 4048,
  'status': True},
 {'description': 'DefaultVlan',
  'interface': 'VLAN 1',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 1001,
  'status': True},
 {'description': '',
  'interface': 'VLAN 180',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 1180,
  'status': False},
 {'description': '',
  'interface': 'VLAN 48',
  'mac': '70:72:CF:13:A1:40',
  'snmp_ifindex': 1048,
  'status': True}]
    motd = ' \n\n      CLI session with the ES3528M is opened.\n      To end the CLI session, enter [Exit].\n\nNo configured settings for reloading.\n'
    cli = {
'terminal length 0':  'terminal length 0\n', 
}
    snmp_get = {}
    snmp_getnext = {'1.3.6.1.2.1.2.2.1.2': [('1.3.6.1.2.1.2.2.1.2.1',
                          'Ethernet Port on unit 1, port 1'),
                         ('1.3.6.1.2.1.2.2.1.2.2',
                          'Ethernet Port on unit 1, port 2'),
                         ('1.3.6.1.2.1.2.2.1.2.3',
                          'Ethernet Port on unit 1, port 3'),
                         ('1.3.6.1.2.1.2.2.1.2.4',
                          'Ethernet Port on unit 1, port 4'),
                         ('1.3.6.1.2.1.2.2.1.2.5',
                          'Ethernet Port on unit 1, port 5'),
                         ('1.3.6.1.2.1.2.2.1.2.6',
                          'Ethernet Port on unit 1, port 6'),
                         ('1.3.6.1.2.1.2.2.1.2.7',
                          'Ethernet Port on unit 1, port 7'),
                         ('1.3.6.1.2.1.2.2.1.2.8',
                          'Ethernet Port on unit 1, port 8'),
                         ('1.3.6.1.2.1.2.2.1.2.9',
                          'Ethernet Port on unit 1, port 9'),
                         ('1.3.6.1.2.1.2.2.1.2.10',
                          'Ethernet Port on unit 1, port 10'),
                         ('1.3.6.1.2.1.2.2.1.2.11',
                          'Ethernet Port on unit 1, port 11'),
                         ('1.3.6.1.2.1.2.2.1.2.12',
                          'Ethernet Port on unit 1, port 12'),
                         ('1.3.6.1.2.1.2.2.1.2.13',
                          'Ethernet Port on unit 1, port 13'),
                         ('1.3.6.1.2.1.2.2.1.2.14',
                          'Ethernet Port on unit 1, port 14'),
                         ('1.3.6.1.2.1.2.2.1.2.15',
                          'Ethernet Port on unit 1, port 15'),
                         ('1.3.6.1.2.1.2.2.1.2.16',
                          'Ethernet Port on unit 1, port 16'),
                         ('1.3.6.1.2.1.2.2.1.2.17',
                          'Ethernet Port on unit 1, port 17'),
                         ('1.3.6.1.2.1.2.2.1.2.18',
                          'Trunk Member Port on Trunk ID 0'),
                         ('1.3.6.1.2.1.2.2.1.2.19',
                          'Trunk Member Port on Trunk ID 0'),
                         ('1.3.6.1.2.1.2.2.1.2.20',
                          'Ethernet Port on unit 1, port 20'),
                         ('1.3.6.1.2.1.2.2.1.2.21',
                          'Ethernet Port on unit 1, port 21'),
                         ('1.3.6.1.2.1.2.2.1.2.22',
                          'Ethernet Port on unit 1, port 22'),
                         ('1.3.6.1.2.1.2.2.1.2.23',
                          'Ethernet Port on unit 1, port 23'),
                         ('1.3.6.1.2.1.2.2.1.2.24',
                          'Ethernet Port on unit 1, port 24'),
                         ('1.3.6.1.2.1.2.2.1.2.25',
                          'Ethernet Port on unit 1, port 25'),
                         ('1.3.6.1.2.1.2.2.1.2.26',
                          'Ethernet Port on unit 1, port 26'),
                         ('1.3.6.1.2.1.2.2.1.2.27',
                          'Ethernet Port on unit 1, port 27'),
                         ('1.3.6.1.2.1.2.2.1.2.28',
                          'Ethernet Port on unit 1, port 28'),
                         ('1.3.6.1.2.1.2.2.1.2.53', 'Trunk ID 0001'),
                         ('1.3.6.1.2.1.2.2.1.2.61', 'Console port'),
                         ('1.3.6.1.2.1.2.2.1.2.1001', 'VLAN ID 0001'),
                         ('1.3.6.1.2.1.2.2.1.2.1048', 'VLAN ID 0048'),
                         ('1.3.6.1.2.1.2.2.1.2.1052', 'VLAN ID 0052'),
                         ('1.3.6.1.2.1.2.2.1.2.1058', 'VLAN ID 0058'),
                         ('1.3.6.1.2.1.2.2.1.2.1180', 'VLAN ID 0180'),
                         ('1.3.6.1.2.1.2.2.1.2.1848', 'VLAN ID 0848'),
                         ('1.3.6.1.2.1.2.2.1.2.4048', 'VLAN ID 3048'),
                         ('1.3.6.1.2.1.2.2.1.2.5000', 'VLAN ID 4000')],
 '1.3.6.1.2.1.2.2.1.6': [('1.3.6.1.2.1.2.2.1.6.1', 'pr\xcf\x13\xa1A'),
                         ('1.3.6.1.2.1.2.2.1.6.2', 'pr\xcf\x13\xa1B'),
                         ('1.3.6.1.2.1.2.2.1.6.3', 'pr\xcf\x13\xa1C'),
                         ('1.3.6.1.2.1.2.2.1.6.4', 'pr\xcf\x13\xa1D'),
                         ('1.3.6.1.2.1.2.2.1.6.5', 'pr\xcf\x13\xa1E'),
                         ('1.3.6.1.2.1.2.2.1.6.6', 'pr\xcf\x13\xa1F'),
                         ('1.3.6.1.2.1.2.2.1.6.7', 'pr\xcf\x13\xa1G'),
                         ('1.3.6.1.2.1.2.2.1.6.8', 'pr\xcf\x13\xa1H'),
                         ('1.3.6.1.2.1.2.2.1.6.9', 'pr\xcf\x13\xa1I'),
                         ('1.3.6.1.2.1.2.2.1.6.10', 'pr\xcf\x13\xa1J'),
                         ('1.3.6.1.2.1.2.2.1.6.11', 'pr\xcf\x13\xa1K'),
                         ('1.3.6.1.2.1.2.2.1.6.12', 'pr\xcf\x13\xa1L'),
                         ('1.3.6.1.2.1.2.2.1.6.13', 'pr\xcf\x13\xa1M'),
                         ('1.3.6.1.2.1.2.2.1.6.14', 'pr\xcf\x13\xa1N'),
                         ('1.3.6.1.2.1.2.2.1.6.15', 'pr\xcf\x13\xa1O'),
                         ('1.3.6.1.2.1.2.2.1.6.16', 'pr\xcf\x13\xa1P'),
                         ('1.3.6.1.2.1.2.2.1.6.17', 'pr\xcf\x13\xa1Q'),
                         ('1.3.6.1.2.1.2.2.1.6.18', 'pr\xcf\x13\xa1R'),
                         ('1.3.6.1.2.1.2.2.1.6.19', 'pr\xcf\x13\xa1S'),
                         ('1.3.6.1.2.1.2.2.1.6.20', 'pr\xcf\x13\xa1T'),
                         ('1.3.6.1.2.1.2.2.1.6.21', 'pr\xcf\x13\xa1U'),
                         ('1.3.6.1.2.1.2.2.1.6.22', 'pr\xcf\x13\xa1V'),
                         ('1.3.6.1.2.1.2.2.1.6.23', 'pr\xcf\x13\xa1W'),
                         ('1.3.6.1.2.1.2.2.1.6.24', 'pr\xcf\x13\xa1X'),
                         ('1.3.6.1.2.1.2.2.1.6.25', 'pr\xcf\x13\xa1Y'),
                         ('1.3.6.1.2.1.2.2.1.6.26', 'pr\xcf\x13\xa1Z'),
                         ('1.3.6.1.2.1.2.2.1.6.27', 'pr\xcf\x13\xa1['),
                         ('1.3.6.1.2.1.2.2.1.6.28', 'pr\xcf\x13\xa1\\'),
                         ('1.3.6.1.2.1.2.2.1.6.53', 'pr\xcf\x13\xa1R'),
                         ('1.3.6.1.2.1.2.2.1.6.61',
                          '\x00\x00\x00\x00\x00\x00'),
                         ('1.3.6.1.2.1.2.2.1.6.1001', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.1048', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.1052', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.1058', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.1180', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.1848', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.4048', 'pr\xcf\x13\xa1@'),
                         ('1.3.6.1.2.1.2.2.1.6.5000', 'pr\xcf\x13\xa1@')],
 '1.3.6.1.2.1.2.2.1.8': [('1.3.6.1.2.1.2.2.1.8.1', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.2', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.3', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.4', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.5', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.6', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.7', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.8', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.9', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.10', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.11', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.12', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.13', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.14', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.15', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.16', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.17', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.18', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.19', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.20', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.21', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.22', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.23', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.24', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.25', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.26', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.27', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.28', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.53', '7'),
                         ('1.3.6.1.2.1.2.2.1.8.61', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1001', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1048', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1052', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1058', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.1180', '2'),
                         ('1.3.6.1.2.1.2.2.1.8.1848', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.4048', '1'),
                         ('1.3.6.1.2.1.2.2.1.8.5000', '1')],
 '1.3.6.1.2.1.31.1.1.1.18': [('1.3.6.1.2.1.31.1.1.1.18.1',
                              'ind40-1-riko.old.office'),
                             ('1.3.6.1.2.1.31.1.1.1.18.2',
                              'eng126-riko.studio'),
                             ('1.3.6.1.2.1.31.1.1.1.18.3',
                              'eng126-riko-loop'),
                             ('1.3.6.1.2.1.31.1.1.1.18.4', 'kosyg/osip-Gldn'),
                             ('1.3.6.1.2.1.31.1.1.1.18.5', 'koltush.loop'),
                             ('1.3.6.1.2.1.31.1.1.1.18.6', 'koltush'),
                             ('1.3.6.1.2.1.31.1.1.1.18.7', 'osupenko4.seg48'),
                             ('1.3.6.1.2.1.31.1.1.1.18.8', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.9', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.10', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.11', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.12', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.13', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.14', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.15', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.16', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.17', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.18', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.19', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.20', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.21', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.22', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.23', 'nastavn-36-2'),
                             ('1.3.6.1.2.1.31.1.1.1.18.24', 'Kosygina-30-2'),
                             ('1.3.6.1.2.1.31.1.1.1.18.25', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.26', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.27', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.28', 'uplink'),
                             ('1.3.6.1.2.1.31.1.1.1.18.53', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.61', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.1001', 'DefaultVlan'),
                             ('1.3.6.1.2.1.31.1.1.1.18.1048', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.1052', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.1058', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.1180', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.1848', ''),
                             ('1.3.6.1.2.1.31.1.1.1.18.4048',
                              'e38-eng126.riko'),
                             ('1.3.6.1.2.1.31.1.1.1.18.5000', '')]}
    http_get = {}
