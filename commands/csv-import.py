# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Import data from CSV
# ---------------------------------------------------------------------
# Copyright (C) 2007-2011 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import with_statement, print_function
import argparse
import sys
# Django modules
from django.db import models
# NOC modules
from noc.sa.models.managedobject import ManagedObject  # noqa
from noc.core.management.base import BaseCommand, CommandError
from noc.core.debug import error_report
from noc.core.csvutils import csv_import, IR_FAIL, IR_SKIP, IR_UPDATE


class Command(BaseCommand):
    help = "Import data from csv file"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--resolve",
                            dest="resolve",
                            action="store",
                            default="fail",
                            ),
        parser.add_argument("-d", "--delimiter",
                            dest="delimiter",
                            action="store",
                            default=",",
                            ),
        parser.add_argument(
            "args",
            nargs=argparse.REMAINDER,
            help="List of extractor names"
        )

    def _usage(self):
        print("Usage:")
        print("%s csv-import [--resolve=action] [--delimiter=<char>] <model> <file1> .. <fileN>" % (sys.argv[0]))
        print("<action> is one of:")
        print("        fail - fail when record is already exists")
        print("        skip - skip duplicated records")
        print("        update - update duplicated records")
        print("<model> is one of:")
        for m in models.get_models():
            t = m._meta.db_table
            app, model = t.split("_", 1)
            print("%s.%s" % (app, model))
        sys.exit(1)

    def handle(self, *args, **options):
        try:
            self._handle(*args, **options)
        except CommandError as why:
            raise CommandError(why)
        except SystemExit:
            pass
        except Exception:
            error_report()

    def _handle(self, *args, **options):
        if len(args) < 1:
            self._usage()
        r = args[0].split(".")
        if len(r) != 2:
            self._usage()
        app, model = r
        m = models.get_model(app, model)
        if not m:
            return self._usage()
        #
        try:
            resolve = {
                "fail": IR_FAIL,
                "skip": IR_SKIP,
                "update": IR_UPDATE
            }[options["resolve"]]
        except KeyError:
            raise CommandError("Invalid resolve option: %s" % options["resolve"])
        # Begin import
        for f in args[1:]:
            print("Importing %s" % f)
            with open(f) as f:
                count, error = csv_import(m, f, resolution=resolve,
                                          delimiter=options["delimiter"])
                if count is None:
                    raise CommandError(error)
                else:
                    print("... %d rows imported/updated" % count)


if __name__ == "__main__":
    Command().run()
