## -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## MAC Database History
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.nosql import (Document, StringField, DateTimeField,
                           IntField)


class MACLog(Document):
    """
    Customer MAC address changes
    """
    meta = {
        "collection": "noc.mac_log",
        "allow_inheritance": False,
        "indexes": ["mac", "-timestamp"]
    }
    # Todo: Add Validation
    timestamp = DateTimeField()
    mac = StringField()
    vlan = IntField()
    managed_object_name = StringField()
    interface_name = StringField()
