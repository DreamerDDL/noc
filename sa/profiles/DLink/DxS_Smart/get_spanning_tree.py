# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# DLink.DxS.get_spanning_tree
# ---------------------------------------------------------------------
# Copyright (C) 2007-2016 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
import itertools
import struct
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetspanningtree import IGetSpanningTree
from noc.sa.interfaces.base import (MACAddressParameter, IntParameter)
from noc.lib.text import parse_table


class Script(BaseScript):
    name = "DLink.DxS_Smart.get_spanning_tree"
    interface = IGetSpanningTree

    STP_MODE = {0: "STP", 1: "STP", 2: "RSTP", 3: "MSTP"}
    PORT_STATE = {
        1: "disabled",
        2: "blocking",
        3: "listen",
        4: "learning",
        5: "forwarding",
        6: "broken",
    }
    PORT_ROLE = {
    }

    def execute(self):
        r = {
            "mode": "None",
            "instances": []
        }
        if self.has_snmp():
            try:
                pmib = self.snmp.get("1.3.6.1.2.1.1.2.0") #SNMPv2-MIB::sysObjectID.0
                v = self.snmp.get(pmib + ".6.1.1.0")
                r["mode"] = self.STP_MODE[v]
                # @todo: DES-1210-10/ME/A1 has another OID pmib + .6.1.9.0
                des_root = self.snmp.get(pmib + ".6.1.8.0")
                instance = { 
                    "id": 0, 
                    "vlans": "1-4095",
                    "root_id": MACAddressParameter().clean(des_root[-6:]),
                    "root_priority": struct.unpack("!H",des_root[:2])[0],
                    "bridge_id": "00:20:00:00:00:00",
                    "bridge_priority": 4096,
                    "interfaces": []
                }
                stp = self.snmp.get_tables(
                    [
                      pmib+".6.2.1.2",pmib+".6.2.1.3", pmib+".6.2.1.9", 
                      pmib+".6.2.1.10",pmib+".6.2.1.13", pmib+".6.2.1.15"
                    ], bulk=True)

                for (port,prio,state,des_bridge,des_port,edge,p2p) in stp:
                    iface = {
                        'interface': port,
                        'port_id': "%d.%s" % (prio,port),
                        'state': self.PORT_STATE[state],
                        'role': 'disabled',
                        'priority': prio,
                        'designated_bridge_id': 
                            MACAddressParameter().clean(des_bridge[-6:]),
                        'designated_bridge_priority': 
                            struct.unpack("!H",des_bridge[:2])[0],
                        'designated_port_id': "%d.%d" %
                            (ord(des_port[0]),ord(des_port[-1])),
                        'point_to_point': int(p2p) == 1,
                        'edge': int(edge) == 1
                    }
                    instance["interfaces"] += [iface]
                r["instances"] += [instance]

            except self.snmp.TimeOutError:
                pass
        return r
