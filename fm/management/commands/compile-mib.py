# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Compile loaded MIB to the compact JSON representation
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from __future__ import with_statement
import sys
import os
from optparse import make_option
import gzip
## Django modules
from django.core.management.base import BaseCommand, CommandError
## NOC modules
from noc.fm.models import MIB, MIBData
from noc.lib.serialize import json_encode


class Command(BaseCommand):
    help = "Compile loaded MIB to compact JSON form"

    option_list = BaseCommand.option_list + (
        make_option("-o", "--output", dest="output", default=""),
        make_option("-l", "--list", dest="list", default="")
    )

    def handle(self, *args, **options):
        job = []  # List of (MIB name, out path)
        mib_list = options.get("list")
        if mib_list:
            with open(mib_list) as f:
                for l in f:
                    l = l.strip()
                    if not l:
                        continue
                    m, p = l.strip().split(",", 1)
                    job += [(m, p)]
        else:
            if len(args) != 1:
                raise CommandError("Single MIB name required")
            job = [(args[0], options.get("output"))]

        # Compile
        for mib_name, path in job:
            try:
                mib = MIB.objects.get(name=mib_name)
            except MIB.DoesNotExist:
                raise CommandError("MIB not loaded: '%s'" % mib_name)
            self.compile_mib(mib, path)

    def compile_mib(self, mib, out_path):
        sys.stderr.write("%s -> %s\n" % (mib.name, out_path))
        if out_path:
            d = os.path.dirname(out_path)
            if not os.path.isdir(d):
                os.makedirs(d)
            if os.path.splitext(out_path)[-1] == ".gz":
                out = gzip.GzipFile(out_path, "w")
            else:
                out = open(out_path, "w")
        else:
            out = sys.stdout

        # Prepare MIB data
        mib_data = []
        for d in MIBData.objects.filter(mib=mib.id).order_by("oid"):
            mib_data += [{
                "oid": d.oid,
                "name": d.name,
                "description": d.description,
                "syntax": d.syntax
            }]
        # Prepare MIB
        if mib.last_updated:
            last_updated = mib.last_updated.strftime("%Y-%m-%d")
        else:
            last_updated = "1970-01-01"
        data = {
            "name": mib.name,
            "description": mib.description,
            "last_updated": last_updated,
            "depends_on": mib.depends_on,
            "typedefs": mib.typedefs,
            "data": mib_data
        }
        # Serialize
        out.write(json_encode(data))
        if out_path:
            out.close()
