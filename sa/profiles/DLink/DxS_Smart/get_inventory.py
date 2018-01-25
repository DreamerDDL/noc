# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# DLink.DxS_Smart.get_inventory
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetinventory import IGetInventory
from noc.sa.interfaces.base import InterfaceTypeError
from noc.sa.profiles.DLink.DxS import get_platform

class Script(BaseScript):
    name = "DLink.DxS_Smart.get_inventory"
    interface = IGetInventory

    def execute(self):
        r = []
        stacks = []
        s = self.scripts.get_version()
        platform = s["platform"]
        revision = s["attributes"]["HW version"]
        p = {
            "type": "CHASSIS",
            "vendor": "DLINK",
            "part_no": get_platform(platform, revision),
            "revision": revision,
            "serial": s["attributes"]["Serial Number"],
            "description": platform
        }
        return [p]
