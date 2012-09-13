# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Vendor: D-Link
## OS:     DxS
## Compatible:
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import re
## NOC modules
from noc.sa.profiles import Profile as NOCProfile


class Profile(NOCProfile):
    name = "DLink.DxS"
    supported_schemes = [NOCProfile.TELNET, NOCProfile.SSH]
    pattern_username = "([Uu]ser ?[Nn]ame|[Ll]ogin):"
    pattern_password = "[Pp]ass[Ww]ord:"
    pattern_more = "CTRL\+C.+?a All"
    pattern_unpriveleged_prompt = r"^\S+:(3|6|user|operator)#"
    pattern_syntax_error = r"(Available commands|Next possible completions|Ambiguous token):"
    command_super = "enable admin"
    pattern_prompt = r"^(?P<hostname>\S+(:\S+)*)#"
    command_disable_pager = "disable clipaging"
    command_more = "a"
    command_exit = "logout"
    command_save_config = "save"
    config_volatile = ["^%.*?$"]
    ##
    ## Version comparison
    ## Version format:
    ## <major>.<minor><sep><patch>
    ##
    rx_ver = re.compile(r"\d+")

    def cmp_version(self, x, y):
        return cmp([int(z) for z in self.rx_ver.findall(x)],
            [int(z) for z in self.rx_ver.findall(y)])

    cluster_member = None
    dlink_pager = False
    rx_pager = re.compile(
        r"^(Clipaging|CLI Paging)\s+:\s*(?P<cp>Enabled|Disabled)\s*$",
        re.MULTILINE)

    def setup_session(self, script):
        # Cache "show switch" command and fetch CLI Paging from it
        match = self.rx_pager.search(script.cli("show switch", cached=True))
        if match:
            self.dlink_pager = (match.group("cp") == "Enabled")

        # Parse path parameters
        for p in script.access_profile.path.split("/"):
            if p.startswith("cluster:"):
                self.cluster_member = p[8:].strip()
            # Switch to cluster member, if necessary
        if self.cluster_member:
            script.debug("Switching to SIM member '%s'" % script.cluster_member)
            script.cli("reconfig member_id %s" % script.cluster_member)

    def shutdown_session(self, script):
        if self.cluster_member:
            script.cli("reconfig exit")
        if self.dlink_pager:
            script.cli("enable clipaging")
        else:
            script.cli("disable clipaging")

    rx_port = re.compile(r"^\s*(?P<port>\d+(/|:)?\d*)\s*"
        r"(\((?P<media_type>(C|F))\))?\s+(?P<admin_state>Enabled|Disabled)\s+"
        r"(?P<admin_speed>Auto|10M|100M|1000M|10G)/"
        r"((?P<admin_duplex>Half|Full)/)?"
        r"(?P<admin_flowctrl>Enabled|Disabled)\s+"
        r"(?P<status>LinkDown|Link\sDown)?((?P<speed>10M|100M|1000M|10G)/"
        r"(?P<duplex>Half|Full)/(?P<flowctrl>None|802.3x))?\s+"
        r"(?P<address_learning>Enabled|Disabled)\s*"
        r"((?P<trap_state>Enabled|Disabled)\s*)?"
        r"(\n\s+(?P<mdix>Auto|MDI|MDIX|\-)\s*)?"
        r"\n\s+Desc(ription)?:\s*?(?P<desc>.*?)$",
        re.MULTILINE)


    def parse_interface(self, s):
        match = self.rx_port.search(s)
        if match:
            port = match.group("port")
            media_type = match.group("media_type")
            obj = {
                "port": port,
                "media_type": media_type,
                "admin_state": match.group("admin_state") == "Enabled",
                "admin_speed": match.group("admin_speed"),
                "admin_duplex": match.group("admin_duplex"),
                "admin_flowctrl": match.group("admin_flowctrl"),
                "status": match.group("status") is None,
                "speed": match.group("speed"),
                "duplex": match.group("duplex"),
                "flowctrl": match.group("flowctrl"),
                "address_learning": match.group("address_learning").strip(),
                "mdix": match.group("mdix"),
                "trap_state": match.group("trap_state"),
                "desc": match.group("desc").strip()
            }
            key = "%s-%s" % (port, media_type)
            return key, obj, s[match.end():]
        else:
            return None

    def get_ports(self, script):
        objects = script.cli_object_stream(
            "show ports description", parser=self.parse_interface,
            cmd_next="n", cmd_stop="q")
        prev_i = None
        ports = []
        for i in objects:
            if prev_i and (prev_i['port'] == i['port']):
                if i['status'] == True:
                    for j in ports:
                        if j['port'] == i['port']:
                            j = i
                            break
            else:
                ports += [i]
            prev_i = i
        return ports

    rx_vlan = re.compile(r"VID\s+:\s+(?P<vlan_id>\d+)\s+"
    r"VLAN Name\s+:\s+(?P<vlan_name>\S+)\s*\n"
    r"VLAN Type\s+:\s+(?P<vlan_type>\S+)\s*.+?"
    r"^(Current Tagged P|Tagged p)orts\s+:\s*(?P<tagged_ports>\S*?)\s*\n"
    r"^(Current Untagged P|Untagged p)orts\s*:\s*(?P<untagged_ports>\S*?)\s*\n",
    re.IGNORECASE | re.MULTILINE | re.DOTALL)

    def get_vlans(self, script):
        vlans = []
        for match in self.rx_vlan.finditer(script.cli("show vlan")):
            tagged_ports = \
                script.expand_interface_range(match.group("tagged_ports"))
            untagged_ports = \
                script.expand_interface_range(match.group("untagged_ports"))
            vlans += [{
                "vlan_id": int(match.group("vlan_id")),
                "vlan_name": match.group("vlan_name"),
                "vlan_type": match.group("vlan_type"),
                "tagged_ports": tagged_ports,
                "untagged_ports": untagged_ports
            }]
        return vlans

def DES3200(v):
    """
    DES-3200-series
    :param v:
    :return:
    """
    return v["platform"].startswith("DES-3200")


def DGS3120(v):
    """
    DGS-3120-series
    :param v:
    :return:
    """
    return v["platform"].startswith("DGS-3120")


def DGS3400(v):
    """
    DGS-3400-series
    :param v:
    :return:
    """
    return ("DGS-3420" not in v["platform"] and
            v["platform"].startswith("DGS-34"))


def DGS3420(v):
    """
    DGS-3420-series
    :param v:
    :return:
    """
    return v["platform"].startswith("DGS-3420")


def DGS3600(v):
    """
    DGS-3600-series
    :param v:
    :return:
    """
    return ("DGS-3610" not in v["platform"] and
            "DGS-3620" not in v["platform"] and
            v["platform"].startswith("DGS-36"))


def DGS3620(v):
    """
    DGS-3620-series
    :param v:
    :return:
    """
    return v["platform"].startswith("DGS-3620")
