# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from django.db import models

class Migration:
    
    def forwards(self):
        db.drop_column("vc_vc","type_id")
        db.execute("ALTER TABLE vc_vcdomain ALTER COLUMN type_id SET NOT NULL")    
    
    def backwards(self):
        "Write your backwards migration here"
