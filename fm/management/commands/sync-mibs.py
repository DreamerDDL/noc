# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Upload bundled MIBs
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from __future__ import with_statement
import os
from optparse import make_option
import gzip
import re
import datetime
import time
## Django modules
from django.core.management.base import BaseCommand, CommandError
## NOC modules
from noc.fm.models import MIB, MIBData
from noc.lib.serialize import json_decode


class Command(BaseCommand):
    help = "Upload bundled MIBs"

    option_list = BaseCommand.option_list + (
        make_option("-f", "--force", dest="force", action="store_true",
                    default=False, help="Force reload"),
    )

    rx_last_updated = re.compile(r"\"last_updated\": \"([^\"]+)\"",
                                 re.MULTILINE)

    def handle(self, *args, **options):
        print "Synchnonizing MIBs"
        self.sync_mibs(force=options["force"])

    def get_bundled_mibs(self):
        """
        Generator returning bundled MIBs list
        :returns: Yields (MIB Name, path)
        """
        for root, dirs, files in os.walk("fm/collections/mibs/"):
            for f in files:
                if (not f.startswith(".") and
                    (f.endswith(".json.gz") or f.endswith(".json"))):
                    mib_name = f.split(".", 1)[0]
                    yield mib_name, os.path.join(root, f)

    def sync_mibs(self, force=False):
        """
        Upload bundled MIBs
        """
        for mib_name, path in self.get_bundled_mibs():
            mib = MIB.objects.filter(name=mib_name).first()
            if path.endswith(".gz"):
                f = gzip.GzipFile(path, "r")
            else:
                f = open(path, "r")
            if mib:
                data = f.read(4096)
                match = self.rx_last_updated.search(data)
                if not match:
                    # Not in first chunk. Read rest
                    data += f.read()
                    match = self.rx_last_updated.search(data)
                last_updated = self.decode_date(match.group(1))
                if (last_updated > mib.last_updated) or force:
                    print "    updating %s" % mib_name
                    self.update_mib(mib, data + f.read())
            else:
                print "    creating %s" % mib_name
                self.create_mib(f.read())
            f.close()

    def decode_date(self, s):
        """
        Convert YYYY-MM-DD date to DateTime
        """
        ts = time.strptime(s, "%Y-%m-%d")
        return datetime.datetime(year=ts.tm_year, month=ts.tm_mon,
                                 day=ts.tm_mday)

    def update_mib(self, mib, data):
        # Deserealize
        d = json_decode(data)
        # Update timestamp
        mib.last_updated = self.decode_date(d["last_updated"])
        mib.save()
        # Upload
        self.upload_mib(mib, d, clean=True)

    def create_mib(self, data):
        # Deserialze
        d = json_decode(data)
        # Create MIB
        mib = MIB(name=d["name"], description=d["description"],
                  last_updated=self.decode_date(d["last_updated"]),
                  depends_on=d["depends_on"])
        mib.save()
        # Upload
        self.upload_mib(mib, d)

    def upload_mib(self, mib, data, clean=False):
        # Prepare new data
        mib_id = mib.id
        for x in data["data"]:
            x["mib"] = mib_id
        if clean:
            # Delete old data
            MIBData.objects.filter(mib=mib_id).delete()
        # Upload new data
        if data["data"]:
            MIBData._get_collection().insert(data["data"])
