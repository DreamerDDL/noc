# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# DLink.DxS_Smart.get_interfaces
# ---------------------------------------------------------------------
# Copyright (C) 2007-2014 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import with_statement
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetinterfaces import IGetInterfaces
from noc.core.ip import IPv4
from noc.core.mib import mib


class Script(BaseScript):
    name = "DLink.DxS_Smart.get_interfaces"
    interface = IGetInterfaces

    rx_ipif = re.compile(r"IP Address\s+:\s+(?P<ip_address>\S+)\s*\n"
    r"Subnet Mask\s+:\s+(?P<ip_subnet>\S+)\s*\n",
    re.IGNORECASE | re.MULTILINE | re.DOTALL)

    rx_mgmt_vlan = re.compile(
        r"^802.1Q Management VLAN\s+: (?P<vlan>\S+)\s*\n")

    def execute(self):
        interfaces = []
        # Get portchannes
        portchannel_members = {}  # member -> (portchannel, type)
        # with self.cached():
        #    for pc in self.scripts.get_portchannel():
        #        i = pc["interface"]
        #        t = pc["type"] == "L"
        #        for m in pc["members"]:
        #            portchannel_members[m] = (i, t)
        admin_status = {}
        ifindexes = {}
        if self.has_snmp():
            try:
                for (oid, i, n, s) in self.snmp.get_tables(
                       [mib["IF-MIB::ifIndex"],
                        mib["IF-MIB::ifName"],
                        mib["IF-MIB::ifAdminStatus"]]):  # IF-MIB
                    if not i or n[:3] == 'Aux' or n[:4] == 'Vlan' \
                    or n[:11] == 'InLoopBack':
                        continue
                    else:
                        n = self.profile.convert_interface_name(n)
                        admin_status.update({n: int(s) == 1})
                        ifindexes.update({n: int(i)})
            except self.snmp.TimeOutError:
                pass
        else:
            ports = self.profile.get_ports(self)
            for p in ports:
                admin_status.update({p['port']: p['admin_state']})
        print "DEBUGA:\n\tadmin_status %r\n\tifindexes %r" % (admin_status, ifindexes)
        lldp = self.get_lldp_ports() 
        stp = self.get_stp_ports() 
        # Get switchports
        for swp in self.scripts.get_switchport():
            admin = admin_status[swp["interface"]]
            ifindex = ifindexes[swp["interface"]]
            name = swp["interface"]
            iface = {
                "name": name,
                "type": "aggregated" if len(swp["members"]) > 0
                else "physical",
                "admin_status": admin,
                "oper_status": swp["status"],
                "enabled_protocols": [],
                # "mac": mac,
                "subinterfaces": [{
                    "name": name,
                    "admin_status": admin,
                    "oper_status": swp["status"],
                    "enabled_afi": ['BRIDGE'],
                    # "mac": mac,
                    "snmp_ifindex": ifindex
                }]
            }
            if swp["tagged"]:
                iface["subinterfaces"][0]["tagged_vlans"] = swp["tagged"]
            try:
                iface["subinterfaces"][0]["untagged_vlan"] = swp["untagged"]
            except KeyError:
                pass
            if 'description' in swp:
                iface["description"] = swp["description"]
            if name in portchannel_members:
                iface["aggregated_interface"] = portchannel_members[name][0]
                if portchannel_members[name][1]:
                    n["enabled_protocols"] = ["LACP"]
            if name in lldp:
              iface["enabled_protocols"] += ["LLDP"]
            if name in stp:
              iface["enabled_protocols"] += ["STP"]
            interfaces += [iface]

        ipif = self.cli("show ipif")
        match = self.rx_ipif.search(ipif)
        if match:
            i = {
                "name": "System",
                "type": "SVI",
                "admin_status": True,
                "oper_status": True,
                "subinterfaces": [{
                    "name": "System",
                    "admin_status": True,
                    "oper_status": True,
                    "enabled_afi": ["IPv4"]
                }]
            }
            ip_address = match.group("ip_address")
            ip_subnet = match.group("ip_subnet")
            ip_address = \
                "%s/%s" % (ip_address, IPv4.netmask_to_len(ip_subnet))
            i['subinterfaces'][0]["ipv4_addresses"] = [ip_address]
            ch_id = self.scripts.get_chassis_id()
            i["mac"] = ch_id[0]['first_chassis_mac']
            i['subinterfaces'][0]["mac"] = ch_id[0]['first_chassis_mac']
            mgmt_vlan = 1
            sw = self.cli("show switch", cached=True)
            match = self.rx_mgmt_vlan.search(ipif)
            if match:
                vlan = match.group("vlan")
                if vlan != "Disabled":
                    vlans = self.profile.get_vlans(self)
                    for v in vlans:
                        if vlan == v['name']:
                            mgmt_vlan = int(v['vlan_id'])
                            break
            # Need hardware to testing
            i['subinterfaces'][0].update({"vlan_ids": [mgmt_vlan]})
            interfaces += [i]

        return [{"interfaces": interfaces}]

    def get_lldp_ports(self):
        lldp = []
        if self.has_snmp():
            try:
                pmib = self.snmp.get("1.3.6.1.2.1.1.2.0") #SNMPv2-MIB::sysObjectID.0
                lldp_enabled = self.snmp.get(pmib + ".24.1.0")
                if lldp_enabled != 1: #dlinklldpState :enabled(1)
                    return lldp
                for oid, v in self.snmp.get_table("1.0.8802.1.1.2.1.1.6.1.2"):
                    if v != 4: #disabled
                      lldp += [oid] 
            except self.snmp.TimeOutError:
                pass
        return lldp

    def get_stp_ports(self):
        stp = []
        if self.has_snmp():
            try:
                pmib = self.snmp.get("1.3.6.1.2.1.1.2.0") #SNMPv2-MIB::sysObjectID.0
                stp_enabled = self.snmp.get(pmib + ".6.1.1.0")
                if stp_enabled != 1: #stpModuleStatus :enabled(1)
                    return stp
                for oid, v in self.snmp.get_table("1.3.6.1.2.1.17.2.15.1.4"):
                    if v == 1: #enabled
                      stp += [oid] 
            except self.snmp.TimeOutError:
                pass
        return stp
