# -*- coding: utf-8 -*-

from south.db import db
from django.db import models


class Migration:
    def forwards(self):
        db.add_column("dns_dnsserver", "sync_channel",
            models.CharField(_("Sync channel"),
                max_length=64, blank=True, null=True))

    def backwards(self):
        db.delete_column("dns_dnsserver", "sync_channel")
