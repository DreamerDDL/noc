## -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## StorageRule
##----------------------------------------------------------------------
## Copyright (C) 2007-2014 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import hashlib
import base64
## Third-party modules
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import (EmbeddedDocumentField, ListField,
                                StringField, IntField, FloatField)
import mongoengine.signals
## NOC modules
from storage import Storage
from noc.lib.nosql import PlainReferenceField


UNITS = {
    "s": 1,
    "m": 60,
    "h": 60 * 60,
    "d": 24 * 60 * 60,
    "w": 7 * 24 * 60 * 60,
    "y": 365 * 24 * 60 * 60
}

unit_choices = [(x, x) for x in UNITS]


class RetentionRule(EmbeddedDocument):
    meta = {
        "allow_inheritance": False
    }
    precision = IntField()
    precision_unit = StringField(default="s", choices=unit_choices)
    duration = IntField()
    duration_unit = StringField(default="s", choices=unit_choices)

    def __unicode__(self):
        return "%s%s:%s%s" % (
            self.precision, self.precision_unit.upper(),
            self.duration, self.duration_unit.upper()
        )

    def get_retention(self):
        """
        Return retention config (precision, points)
        """
        precision = self.precision * UNITS[self.precision_unit]
        points = (self.duration * UNITS[self.duration_unit]) / precision
        return precision, points


class StorageRule(Document):
    meta = {
        "collection": "noc.storagerules",
        "allow_inheritance": False
    }
    name = StringField(unique=True)
    description = StringField(required=False)
    storage = PlainReferenceField(Storage)
    aggregation_method = StringField(
        default="average",
        choices=[
            ("average", "Average"),
            ("sum", "Sum"),
            ("max", "Max"),
            ("min", "Min"),
            ("last", "Last")
        ]
    )
    retentions = ListField(EmbeddedDocumentField(RetentionRule))
    xfilesfactor = FloatField(required=False,
                              min_value=0.0, max_value=1.0)

    def __unicode__(self):
        return self.name

    def get_retention(self):
        return [r.get_retention() for r in self.retentions]

    def get_interval(self):
        return self.retentions[0].get_retention()[0]

    @property
    def sr_id(self):
        return base64.b32encode(hashlib.md5(str(self.id)).digest())[:6]


##
from probeconfig import ProbeConfig
mongoengine.signals.post_save.connect(
    ProbeConfig.on_change_storage_rule,
    sender=StorageRule
)
