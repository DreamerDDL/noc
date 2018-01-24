# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# DLink.DxS_Smart.get_capabilities
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.sa.profiles.Generic.get_capabilities import Script as BaseScript

class Script(BaseScript):
    name = "DLink.DxS_Smart.get_capabilities"

    def has_stp_snmp(self):
        """
        Check box has STP enabled
        """
        # Spanning Tree Enabled/Disabled : Enabled
        r = False
        if self.has_snmp():
            try:
                pmib = self.snmp.get("1.3.6.1.2.1.1.2.0") #SNMPv2-MIB::sysObjectID.0
                r = self.snmp.get(pmib + ".6.1.1.0", cached=True)  # stpModuleStatus
            except self.snmp.TimeOutError:
                pass
        return r

    def has_lldp_snmp(self):
        """
        Check box has LLDP enabled
        """
        # LLDP Enabled/Disabled : Enabled
        r = False
        if self.has_snmp():
            try:
                v = self.scripts.get_version()
                pmib = self.snmp.get("1.3.6.1.2.1.1.2.0") #SNMPv2-MIB::sysObjectID.0
                companyLLDP = ".24.1.0"
                if v["platform"].startswith("DES-1210-10"):
                    companyLLDP = ".32.1.0"
                r = self.snmp.get(pmib + companyLLDP, cached=True)  # dlinklldpState
            except self.snmp.TimeOutError:
                pass
        return r
