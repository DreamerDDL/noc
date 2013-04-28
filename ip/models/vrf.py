# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## VRF model
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import hashlib
import struct
## Django modules
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import Q
## NOC modules
from noc.main.models import Style, ResourceState, CustomField
from noc.peer.models.asn import AS
from vrfgroup import VRFGroup
from noc.lib.validators import check_rd, is_rd
from noc.lib.fields import TagsField
from noc.lib.app import site
from noc.lib.search import SearchResult


class VRF(models.Model):
    """
    VRF
    """
    class Meta:
        verbose_name = _("VRF")
        verbose_name_plural = _("VRFs")
        db_table = "ip_vrf"
        app_label = "ip"
        ordering = ["name"]

    name = models.CharField(
        _("VRF"),
        unique=True,
        max_length=64,
        help_text=_("Unique VRF Name"))
    vrf_group = models.ForeignKey(
        VRFGroup, verbose_name=_("VRF Group"))
    rd = models.CharField(
        _("RD"),
        unique=True,
        max_length=21,
        validators=[check_rd],
        help_text=_("Route Distinguisher in form of ASN:N or IP:N"))
    afi_ipv4 = models.BooleanField(
        _("IPv4"),
        default=True,
        help_text=_("Enable IPv4 Address Family"))
    afi_ipv6 = models.BooleanField(
        _("IPv6"),
        default=False,
        help_text=_("Enable IPv6 Address Family"))
    description = models.TextField(
        _("Description"), blank=True, null=True)
    tt = models.IntegerField(
        _("TT"),
        blank=True,
        null=True,
        help_text=_("Ticket #"))
    tags = TagsField(_("Tags"), null=True, blank=True)
    style = models.ForeignKey(
        Style,
        verbose_name=_("Style"),
        blank=True,
        null=True)
    state = models.ForeignKey(
        ResourceState,
        verbose_name=_("State"),
        default=ResourceState.get_default)
    allocated_till = models.DateField(
        _("Allocated till"),
        null=True,
        blank=True,
        help_text=_("VRF temporary allocated till the date"))

    def __unicode__(self):
        if self.rd == "0:0":
            return u"global"
        else:
            return self.name

    def get_absolute_url(self):
        return site.reverse("ip:vrf:change", self.id)

    @classmethod
    def get_global(cls):
        """
        Returns VRF 0:0
        """
        return VRF.objects.get(rd="0:0")

    @classmethod
    def generate_rd(cls, name):
        """
        Generate unique rd for given name
        """
        return "0:%d" % struct.unpack(
            "I", hashlib.sha1(name).digest()[:4])

    def save(self, **kwargs):
        """
        Create root entries for all enabled AFIs
        """
        # Generate unique rd, if empty
        if not self.rd:
            self.rd = self.generate_rd(self.name)
        # Save VRF
        super(VRF, self).save(**kwargs)
        if self.afi_ipv4:
            # Create IPv4 root, if not exists
            Prefix.objects.get_or_create(
                vrf=self, afi="4", prefix="0.0.0.0/0",
                defaults={
                    "asn": AS.default_as(),
                    "description": "IPv4 Root"
                })
        if self.afi_ipv6:
            # Create IPv6 root, if not exists
            Prefix.objects.get_or_create(
                vrf=self, afi="6", prefix="::/0",
                defaults={
                    "asn": AS.default_as(),
                    "description": "IPv6 Root"})

    @classmethod
    def search(cls, user, query, limit):
        """
        Search engine plugin
        """
        q = Q(name__icontains=query)
        if is_rd(query):
            q |= Q(rd=query)
        cq = CustomField.table_search_Q(cls._meta.db_table, query)
        if cq:
            q |= cq
        for o in cls.objects.filter(q):
            relevancy = 1.0
            yield SearchResult(
                url=("ip:vrf:change", o.id),
                title="VRF: " + unicode(o),
                text=unicode(o),
                relevancy=relevancy
            )

## Avoid circular references
from prefix import Prefix
