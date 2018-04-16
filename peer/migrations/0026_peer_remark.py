# -*- coding: utf-8 -*-

# Third-party modules
from south.db import db
from django.db import models


class Migration(object):

    def forwards(self):
        db.add_column("peer_peer", "rpsl_remark",
                      models.CharField("RPSL Remark", max_length=64, null=True, blank=True))

    def backwards(self):
        db.delete_column("peer_peer", "rpsl_remark")
