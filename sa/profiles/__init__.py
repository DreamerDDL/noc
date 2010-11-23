# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Profile base class
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
# Python Modules
import re
# NOC Modules
from noc.lib.registry import Registry
from noc.lib.ecma48 import strip_control_sequences
from noc.sa.interfaces import InterfaceTypeError
from noc.lib.ip import *

##
##
##
class ProfileRegistry(Registry):
    name="ProfileRegistry"
    subdir="profiles"
    classname="Profile"
    apps=["noc.sa"]
    exclude=["highlight"]
profile_registry=ProfileRegistry()

##
##
##
class ProfileBase(type):
    def __new__(cls,name,bases,attrs):
        m=type.__new__(cls,name,bases,attrs)
        m.scripts={}
        profile_registry.register(m.name,m)
        return m
##
## Abstract Profile
##
class Profile(object):
    __metaclass__=ProfileBase
    # Profile name
    name=None
    #
    # Device capabilities
    #
    
    #
    # A list of supported access schemes.
    # Access schemes constants are defined
    # in noc.sa.protocols.sae_pb2
    # (TELNET, SSH, HTTP, etc)
    #
    supported_schemes=[]
    # Regular expression to catch user name prompt
    # (Usually during telnet sessions)
    pattern_username="([Uu]sername|[Ll]ogin):"
    # Regulal expression to catch password prompt
    # (Telnet/SSH sessions)
    pattern_password="[Pp]assword:"
    # Regular expression to catch command prompt
    # (CLI Sessions)
    pattern_prompt=r"^\S*[>#]"
    # Regular expression to catch unpriveleged mode command prompt
    # (CLI Session)
    pattern_unpriveleged_prompt=None
    # Regular expression to catch pager
    # (Used in command results)
    # If pattern_more is string, send command_more
    # If pattern_more is a list of (pattern,command)
    # send appropriative command
    pattern_more="^---MORE---"
    # Regular expression to catch the syntax errors in cli output.
    # If CLI output matches pattern_syntax_error, then CLISyntaxError exception raised
    pattern_syntax_error=None
    # Sequence to be send to list forward pager
    # If pattern_more is string and is matched
    command_more="\n"
    # Sequence to be send at the end of all CLI commands
    #
    command_submit="\n"
    # Sequence to disable pager
    #
    command_disable_pager=None
    # Sequence to gracefully close session
    #
    command_exit="exit"
    # Sequence to enable priveleged mode
    #
    command_super=None
    # Sequence to enter configuration mode
    #
    command_enter_config=None
    # Sequence to leave configuration mode
    #
    command_leave_config=None
    # Sequence to save configuration
    #
    command_save_config=None
    # List of chars to be stripped out of input stream
    # before checking any regular expressions
    # (when Action.CLEAN_INPUT==True)
    rogue_chars=["\r"]
    # Does the equipment supports bitlength netmasks
    # or netmask should be converted to traditional formats
    requires_netmask_conversion=False
    #
    # Converts ip prefix to the format acceptable by router
    #
    def convert_prefix(self,prefix):
        if "/" in prefix and self.requires_netmask_conversion:
            p=IPv4(prefix)
            return "%s %s"%(prefix.address,prefix.netmask.address)
        return prefix
    #
    # Leave 00:11:22:33:44:55 style MAC-address untouched
    #
    def convert_mac_to_colon(self,mac):
        return mac
    #
    # Convert 00:11:22:33:44:55 style MAC-address to 0011.2233.4455
    #
    def convert_mac_to_cisco(self,mac):
        v=mac.replace(":","").lower()
        return "%s.%s.%s"%(v[:4],v[4:8],v[8:])
    #
    # Convert 00:11:22:33:44:55 style MAC-address to 00-11-22-33-44-55
    #
    def convert_mac_to_dashed(self,mac):
        v=mac.replace(":","").lower()
        return "%s-%s-%s-%s-%s-%s"%(v[:2],v[2:4],v[4:6],v[6:8],v[8:10],v[10:])
    #
    # Convert 00:11:22:33:44:55 style MAC-address to local format
    # Can be changed in derived classes
    #
    convert_mac=convert_mac_to_colon
    #
    # Interface name normalization
    #
    # Dumb translation
    def convert_interface_name(self,s):
        return s
    # Cisco-like translation
    rx_cisco_interface_name=re.compile(r"^(?P<type>[a-z]{2})[a-z\-]*\s*(?P<number>\d+(/\d+(/\d+)?)?(\.\d+(\.\d+)?)?)$",re.IGNORECASE)
    def convert_interface_name_cisco(self,s):
        """
        >>> Profile().convert_interface_name_cisco("Gi0")
        'Gi 0'
        >>> Profile().convert_interface_name_cisco("GigabitEthernet0")
        'Gi 0'
        >>> Profile().convert_interface_name_cisco("Gi 0")
        'Gi 0'
        >>> Profile().convert_interface_name_cisco("tengigabitethernet 1/0/1")
        'Te 1/0/1'
        >>> Profile().convert_interface_name_cisco("tengigabitethernet 1/0/1.5")
        'Te 1/0/1.5'
        """
        match=self.rx_cisco_interface_name.match(s)
        if not match:
            raise InterfaceTypeError("Invalid interface '%s'"%s)
        return "%s %s"%(match.group("type").capitalize(),match.group("number"))
    #
    # Configuration generators
    #
    
    # Generate prefix list:
    # name - name of prefix list
    # pl -  is a list of prefixes
    # Strict - should tested prefix be exactly matched
    # or should be more specific as well
    #
    def generate_prefix_list(self,name,pl,strict=True):
        raise Excepton("Not implemented")
    #
    # Volatile strings:
    # A list of strings can be changed over time, which
    # can be sweeped out of config safely or None
    # Strings are regexpes, compuled with re.DOTALL|re.MULTILINE
    #
    config_volatile=None
    #
    # Preprocessor to clean up and normalize input from device.
    # Delete ASCII sequences by default.
    # Can be overriden to achieve desired behavior
    #
    def cleaned_input(self,input):
        return strip_control_sequences(input)
    #
    # Clean up config
    #
    def cleaned_config(self,cfg):
        if self.config_volatile:
            # Wipe out volatile strings before returning result
            for r in self.config_volatile:
                rx=re.compile(r,re.DOTALL|re.MULTILINE)
                cfg=rx.sub("",cfg)
        return unicode(cfg,"utf8","ignore").encode("utf8") # Prevent serialization errors
    
    #
    # Compare two versions.
    # Must return:
    #    <0 , if v1<v2
    #     0 , if v1==v2
    #    >0 , if v1>v2
    #  None , if v1 and v2 cannot be compared
    #
    # Default implementation compares versions as strings, which is surely not what you want
    #
    def cmp_version(self,v1,v2):
        return cmp(v1,v2)
    
    #
    # Highligh config
    # Try to include profile's highlight module and use its ConfigLexer
    # Returns escaped HTML
    #
    def highlight_config(self,cfg):
        # Check for pygments available
        try:
            from pygments import highlight
        except ImportError:
            # No pygments, no highlighting. Return escaped HTML
            from django.utils.html import escape
            return "<pre><!--no pygments-->%s</pre>"%escape(cfg).replace("\n","<br/>")
        # Check for lexer available
        from pygments.lexers import TextLexer
        from noc.lib.highlight import NOCHtmlFormatter
        
        lexer=None
        for l in ["local.",""]: # Try to import local/ version first
            h_mod="noc.%ssa.profiles.%s.highlight"%(l,self.name)
            try:
                m=__import__(h_mod,{},{},"ConfigLexer")
                lexer=m.ConfigLexer
                break
            except ImportError:
                continue
            except AttributeError:
                continue
        if not lexer:
            lexer=TextLexer
        # Return highlighted text
        return highlight(cfg, lexer(), NOCHtmlFormatter())
