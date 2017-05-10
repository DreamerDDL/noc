# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Raisecom.RCIOS.get_interfaces
##----------------------------------------------------------------------
## Copyright (C) 2007-2017 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import re
from collections import defaultdict
## NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetinterfaces import IGetInterfaces
from noc.lib.text import ranges_to_list
from noc.core.ip import IPv4
from noc.core.ip import IPv6


class Script(BaseScript):
    name = "Raisecom.RCIOS.get_interfaces"
    cache = True
    interface = IGetInterfaces

    rx_iface = re.compile(
        r"Interface\s+(?P<iface>\S+)\s+is\s+(?P<oper>up|down),\s+Admin\s+status\s+is\s+(?P<admin>up|down)\s*\n^\s+aliasname\s+\S+\s*\n(^\s+inet addr:\s+(?P<ip_addr>\S+)\s+(Bcast:\s+\d+\S+\d+\s+)?Mask:\s*(?P<ip_mask>\d+\S+\d+)\s*\n)?(^\s+inet addr6:\s+(?P<ipv6_addr>\S+)\s+Mask:\s*(?P<ipv6_mask>\S+)\s*\n)?(^\s+Hardware address:\s+(?P<mac>\S+)\s*\n)?(^\s+.+?\s+MTU:\s*(?P<mtu>\d+).+?\n)?",
            re.MULTILINE )


    def execute(self):
        interfaces = []
        v = self.cli("show interface", cached=True)
        for match in self.rx_iface.finditer(v):
            ifname = match.group("iface")
            iface = {
                "name": ifname,
                "type": self.profile.get_interface_type(ifname),
                "oper_status": match.group("oper"),
                "admin_status": match.group("admin"),
                "mac": match.group("mac"),
                "subinterfaces": [{
                    "name": ifname,
                    "oper_status": match.group("oper"),
                    "admin_status": match.group("admin"),
                    "mac": match.group("mac"),
                    "enabled_afi": []
                }]
            }
            if match.group("ip_addr"):
            	ip = match.group("ip_addr")
            	netmask = str(IPv4.netmask_to_len(match.group("ip_mask")))
            	ip = ip + '/' + netmask
            	ip_list = [ip]
            	iface["subinterfaces"][0]["ipv4_addresses"] = ip_list
                iface["subinterfaces"][0]["enabled_afi"] += ["IPv4"]

            if match.group("ipv6_addr"):
            	ip = IPv6(match.group("ipv6_addr"))
            	netmask = match.group("ipv6_mask")
            	ip_list = [ip]
            	iface["subinterfaces"][0]["ipv6_addresses"] = ip_list
                iface["subinterfaces"][0]["enabled_afi"] += ["IPv6"]                
            else:
                iface["subinterfaces"][0]["enabled_afi"] += ["BRIDGE"]
            interfaces += [iface]

        return [{"interfaces": interfaces}]

