# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
import socket,struct
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from noc.lib.validators import check_rd,check_cidr,is_cidr,is_ipv4
from noc.lib.tt import tt_url
from noc.peer.models import AS
from noc.lib.fields import CIDRField
from noc.lib.ip import int_to_address,bits_to_int,wildcard,broadcast,address_to_int
from noc.main.menu import Menu
from noc.main.search import SearchResult
##
##
##
class VRFGroup(models.Model):
    class Meta:
        verbose_name="VRF Group"
        verbose_name_plural="VRF Groups"
    name=models.CharField("VRF Group",unique=True,max_length=64)
    unique_addresses=models.BooleanField("Unique addresses in group")
    def __str__(self):
        return self.name
    def __unicode__(self):
        return unicode(self.name)
##
##
##
class VRF(models.Model):
    class Meta:
        verbose_name="VRF"
        verbose_name_plural="VRFs"
    name=models.CharField("VRF name",unique=True,max_length=64)
    vrf_group=models.ForeignKey(VRFGroup,verbose_name="VRF Group")
    rd=models.CharField("rd",unique=True,max_length=21) # validator_list=[check_rd],
    tt=models.IntegerField("TT",blank=True,null=True)
    def __str__(self):
        if self.rd=="0:0":
            return "global"
        return self.rd
    def __unicode__(self):
        if self.rd=="0:0":
            return u"global"
        return self.rd
        
    def prefix(self,top="0.0.0.0/0"):
        assert is_cidr(top)
        return IPv4Block.objects.get(prefix=top,vrf=self)
        
    def prefixes(self,top="0.0.0.0/0"):
        assert is_cidr(top)
        return self.prefix(top).children
        
    def all_prefixes(self,top="0.0.0.0/0"):
        assert is_cidr(top)
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE vrf_id=%d and prefix<<='%s' order by prefix"%(IPv4Block._meta.db_table,self.id,top))
        return [IPv4Block.objects.get(id=x[0]) for x in c.fetchall()]
        
    def all_addresses(self,top="0.0.0.0/0"):
        assert is_cidr(top)
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE vrf_id=%d and ip<<='%s' order by ip"%(IPv4Address._meta.db_table,self.id,top))
        return [IPv4Address.objects.get(id=x[0]) for x in c.fetchall()]
##
##
##
class IPv4BlockAccess(models.Model):
    class Meta:
        verbose_name="IPv4 Block Access"
        verbose_name_plural="IPv4 Block Access"
        unique_together=[("user","vrf","prefix")]
    user=models.ForeignKey(User,verbose_name="User")
    vrf=models.ForeignKey(VRF,verbose_name="VRF")
    prefix=CIDRField("prefix")
    tt=models.IntegerField("TT",blank=True,null=True)
    def __str__(self):
        return "%s: %s(%s)"%(self.user,self.prefix,self.vrf)
    @classmethod
    def check_write_access(self,user,vrf,prefix):
        assert is_cidr(prefix)
        from django.db import connection
        if user.is_superuser:
            return True
        c=connection.cursor()
        c.execute("SELECT COUNT(*) FROM %s WHERE prefix >>= '%s' AND vrf_id=%d AND user_id=%d"%(IPv4BlockAccess._meta.db_table,str(prefix),vrf.id,user.id))
        return c.fetchall()[0][0]>0
##
##
##
class IPv4Block(models.Model):
    class Meta:
        verbose_name="IPv4 Block"
        verbose_name_plural="IPv4 Blocks"
        unique_together=[("prefix","vrf")]
        ordering=["prefix"]
    description=models.CharField("Description",max_length=64)
    prefix=CIDRField("prefix")
    vrf=models.ForeignKey(VRF)
    asn=models.ForeignKey(AS)
    modified_by=models.ForeignKey(User,verbose_name="User")
    last_modified=models.DateTimeField("Last modified",auto_now=True,auto_now_add=True)
    tt=models.IntegerField("TT",blank=True,null=True)
    #allocated_till
    def __str__(self):
        return str(self.prefix)
    def __unicode__(self):
        return unicode(self.prefix)
    def _parent(self):
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE prefix >> '%s' AND vrf_id=%d ORDER BY masklen(prefix) DESC LIMIT 1"%(IPv4Block._meta.db_table,
                    self.prefix,self.vrf.id))
        r=c.fetchall()
        if len(r)==0:
            return
        return IPv4Block.objects.get(id=r[0][0])
    parent=property(_parent)

    def _parents(self):
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE prefix >> '%s' AND vrf_id=%d ORDER BY masklen(prefix)"%(IPv4Block._meta.db_table,
                    self.prefix,self.vrf.id))
        return [IPv4Block.objects.get(id=i[0]) for i in c.fetchall()]
    parents=property(_parents)

    def _depth(self):
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT COUNT(*) FROM %s WHERE prefix >> '%s' AND vrf_id=%d"%(IPv4Block._meta.db_table,self.prefix,self.vrf.id))
        return c.fetchone()[0]
    depth=property(_depth)

    def _children(self):
        from django.db import connection
        c=connection.cursor()
        if self.vrf.vrf_group.unique_addresses:
            vrfs="IN (%s)"%",".join([str(vrf.id) for vrf in self.vrf.vrf_group.vrf_set.all()])
            vg_id=self.vrf.vrf_group.id
            c.execute("SELECT b.id FROM %s b JOIN %s v ON (b.vrf_id=v.id) WHERE b.prefix << '%s' AND v.id %s AND ip_ipv4_block_depth_in_vrf_group(%d,b.prefix,'%s')=0 ORDER BY prefix"%\
                        (IPv4Block._meta.db_table,VRF._meta.db_table,self.prefix,vrfs,vg_id,self.prefix))
        else:
            vrfs="= %d"%self.vrf.id
            c.execute("SELECT b.id FROM %s b JOIN %s v ON (b.vrf_id=v.id) WHERE b.prefix << '%s' AND v.id %s AND ip_ipv4_block_depth(v.id,b.prefix,'%s')=0 ORDER BY prefix"%\
                        (IPv4Block._meta.db_table,VRF._meta.db_table,self.prefix,vrfs,self.prefix))
        return [IPv4Block.objects.get(id=i[0]) for i in c.fetchall()]

    children=property(_children)

    def _has_children(self):
        from django.db import connection
        c=connection.cursor()
        if self.vrf.vrf_group.unique_addresses:
            vrfs="IN (%s)"%",".join([str(vrf.id) for vrf in self.vrf.vrf_group.vrf_set.all()])
        else:
            vrfs="= %d"%self.vrf.id
        data=[]
        c.execute("SELECT COUNT(*) FROM %s b JOIN %s v ON (b.vrf_id=v.id) WHERE b.prefix << '%s' AND v.id %s AND ip_ipv4_block_depth(v.id,b.prefix,'%s')=0"%\
                    (IPv4Block._meta.db_table,VRF._meta.db_table,self.prefix,vrfs,self.prefix))
        return c.fetchall()[0][0]>0
    has_children=property(_has_children)

    def _addresses(self):
        if self.has_children:
            return []
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE vrf_id=%d AND ip << '%s' ORDER BY ip"%(IPv4Address._meta.db_table,self.vrf.id,self.prefix))
        return [IPv4Address.objects.get(id=i[0]) for i in c.fetchall()]
    addresses=property(_addresses)
    ##
    ## Generator returning a nested ip addresses (including nested children)
    ##
    def _nested_addresses(self):
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE vrf_id=%d AND ip << '%s' ORDER BY ip"%(IPv4Address._meta.db_table,self.vrf.id,self.prefix))
        for row in c:
            yield IPv4Address.objects.get(id=row[0])
    nested_addresses=property(_nested_addresses)
    ##
    ## Return a list of all used/unused addresses
    ##
    def _all_addresses(self):
        if self.has_children:
            return None
        a=dict((x.ip,x) for x in self.addresses)
        if len(a)==0:
            return []
        r=[]
        for nip in range(address_to_int(self.network),address_to_int(self.broadcast)+1):
            ip=int_to_address(nip)
            if ip in a:
                r.append(a[ip])
            else:
                r.append(ip)
        return r
    all_addresses=property(_all_addresses)

    def _netmask_bits(self):
        return int(str(self.prefix).split("/")[1])
    netmask_bits=property(_netmask_bits)

    def _netmask(self):
        return int_to_address(bits_to_int(self.netmask_bits))
    netmask=property(_netmask)

    def _network(self):
        return str(self.prefix).split("/")[0]
    network=property(_network)

    def _wildcard(self): 
        return wildcard(self.prefix)
    wildcard=property(_wildcard)

    def _broadcast(self):
        return broadcast(self.prefix)
    broadcast=property(_broadcast)
    
    def _tt_url(self):
        return tt_url(self)
    tt_url=property(_tt_url)
    ##
    ## Search engine plugin
    ##
    @classmethod
    def search(cls,user,search,limit):
        if user.has_perm("ip.change_ipv4block"):
            q=Q(description__icontains=search)
            if is_cidr(search):
                q|=Q(prefix=search)
            for r in IPv4Block.objects.filter(q):
                if search==r.prefix:
                    relevancy=1.0
                else:
                    l=len(r.description)
                    if l:
                        relevancy=float(len(search))/float(l)
                    else:
                        relevancy=0.0
                yield SearchResult(url="/ip/%d/%s/"%(r.vrf.id,r.prefix),
                    title="IPv4 Block, VRF=%s, %s"%(r.vrf,r.prefix),
                    text=r.description,
                    relevancy=relevancy)
##
##
##
class IPv4Address(models.Model):
    class Meta:
        unique_together=[("vrf","ip")]
        verbose_name="IPv4 Address"
        verbose_name_plural="IPv4 Addresses"
        ordering=["ip"]
    vrf=models.ForeignKey(VRF,verbose_name="VRF")
    fqdn=models.CharField("FQDN",max_length=64)
    ip=models.IPAddressField("IP")
    description=models.CharField("Description",blank=True,null=True,max_length=64)
    modified_by=models.ForeignKey(User,verbose_name="User")
    last_modified=models.DateTimeField("Last modified",auto_now=True,auto_now_add=True)
    tt=models.IntegerField("TT",blank=True,null=True)
    
    def __unicode__(self):
        return self.ip

    def __str__(self):
        return self.ip

    def _parent(self):
        from django.db import connection
        c=connection.cursor()
        c.execute("SELECT id FROM %s WHERE vrf_id=%d AND '%s' << prefix ORDER BY masklen(prefix) DESC LIMIT 1"%(IPv4Block._meta.db_table,self.vrf.id,str(self.ip)))
        return IPv4Block.objects.get(id=c.fetchall()[0][0])
    parent=property(_parent)
    
    def _tt_url(self):
        return tt_url(self)
    tt_url=property(_tt_url)
    ##
    ## Search engine
    ##
    @classmethod
    def search(cls,user,search,limit):
        if user.has_perm("ip.change_ipv4address"):
            q=Q(fqdn__icontains=search)|Q(description__icontains=search)
            if is_ipv4(search):
                q|=Q(ip=search)
            for r in IPv4Address.objects.filter(q):
                if search==r.ip:
                    relevancy=1.0
                else:
                    ls=float(len(search))
                    if search in r.fqdn and len(r.fqdn)>0:
                        r_fqdn=ls/float(len(r.fqdn))
                    else:
                        r_fqdn=0.0
                    if search in r.description and len(r.description)>0:
                        r_description=ls/float(len(r.description))
                    else:
                        r_description=0.0
                    relevancy=max(r_fqdn,r_description)
                yield SearchResult(url="/admin/ip/ipv4address/%d/"%r.id,
                    title="IPv4 Address, VRF=%s, %s (%s)"%(r.vrf,r.ip,r.fqdn),
                    text=r.description,
                    relevancy=relevancy)
##
## Application Menu
##
class AppMenu(Menu):
    app="ip"
    title="Address Space Management"
    items=[
        ("Assigned addresses", "/ip/", "ip.change_ipv4block"),
        ("Setup",[
            ("VRF Groups",  "/admin/ip/vrfgroup/",        "ip.change_vrfgroup"),
            ("VRFs",        "/admin/ip/vrf/",             "ip.change_vrf"),
            ("Block Access","/admin/ip/ipv4blockaccess/", "ip.change_ipv4blockaccess"),
            ]
        )
    ]
