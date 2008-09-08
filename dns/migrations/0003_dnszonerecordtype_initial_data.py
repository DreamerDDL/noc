
from south.db import db
from noc.dns.models import *

RECORD_TYPES=[
    ("A",True),
    ("AAAA",True),
    ("AFSDB",False),
    ("AXFR",False),
    ("CERT",False),
    ("CNAME",True),
    ("DHCID",False),
    ("DLV",False),
    ("DNAME",False),
    ("DNSKEY",False),
    ("DS",False),
    ("HIP",False),
    ("IPSECKEY",False),
    ("IXFR",False),
    ("KEY",False),
    ("LOC",False),
    ("MX",True),
    ("NAPTR",True),
    ("NS",True),
    ("NSEC",False),
    ("NSEC3",False),
    ("NSEC3PARAM",False),
    ("OPT",False),
    ("PTR",True),
    ("RRSIG",False),
    ("SIG",False),
    ("SPF",True),
    ("SRV",True),
    ("SSHFP",False),
    ("TA",False),
    ("TKEY",False),
    ("TSIG",False),
    ("TXT",True),
    ]

class Migration:
    def forwards(self):
        for rtype,is_visible in RECORD_TYPES:
            try:
                DNSZoneRecordType.objects.get(type=rtype)
                continue
            except:
                pass
            print "Creating DNSZoneRecordType '%s'"%rtype
            rt=DNSZoneRecordType(type=rtype,is_visible=is_visible)
            rt.save()
    
    def backwards(self):
        "Write your backwards migration here"
