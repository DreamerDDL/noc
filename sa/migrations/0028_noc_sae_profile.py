# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
from south.db import db
from django.db import models

class Migration:
    
    def forwards(self):
        db.execute("UPDATE sa_managedobject SET name=%s,profile_name=%s WHERE name=%s",["SAE","NOC.SAE","ROOT"])
    
    def backwards(self):
        db.execute("UPDATE sa_managedobject SET name=%s,profile_name=%s WHERE name=%s",["ROOT","NOC","SAE"])
