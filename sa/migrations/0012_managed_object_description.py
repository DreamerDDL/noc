# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Third-party modules
from south.db import db


class Migration:
    def forwards(self):
        db.rename_column("sa_managedobject", "location", "description")

    def backwards(self):
        db.rename_column("sa_managedobject", "description", "location")
