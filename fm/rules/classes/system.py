# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## System event classes description
## System events are generated by NOC itself
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
from noc.fm.rules.classes import EventClass,Var
##
## Unhandled python exception in daemon
##
class UnhandledException(EventClass):
    name="Unhandled Exception"
    category="SYSTEM"
    priority="CRITICAL"
    subject_template="Exception: {{component}}"
    body_template="""Unhandled exception at {{component}}
-----------
{{traceback}}
-----------
    """
    class Vars:
        source=Var(required=True)
        type=Var(required=True)
        component=Var(required=True)
        traceback=Var(required=True)
##
## Activator reveived message from unknown source address
##
class InvalidEventSource(EventClass):
    name="Invalid Event Source"
    category="SYSTEM"
    priority="WARNING"
    subject_template="Invalid event source: {{ip}}"
    body_template="""Invalid event source {{ip}} at activator {{activator}}"""
    class Vars:
        source=Var(required=True)
        type=Var(required=True)
        activator=Var(required=True)
        ip=Var(required=True)
##
## Periodic task terminated with failure
##
class PeriodicTaskFailed(EventClass):
    name="Periodic Task Failed"
    category="SYSTEM"
    priority="CRITICAL"
    subject_template="Periodic task failed: {{periodic}}"
    body_template="""Periodic task failed: {{periodic}}"""
    class Vars:
        source=Var(required=True)
        type=Var(required=True)
        periodic=Var(required=True)
##
## Managed Object Unreachable during ping probe
##
class ObjectUnreachable(EventClass):
    name="Object Unreachable"
    category="NETWORK"
    priority="MAJOR"
    subject_template="DOWN: {{ip}}"
    body_template="""Object unreachable: {{ip}}"""
    class Vars:
        source=Var(required=True)
        activator=Var(required=True)
        probe=Var(required=True)
        type=Var(required=True)
        ip=Var(required=True)
##
## Managed Reachable during ping probe
##
class ObjectReachable(EventClass):
    name="Object Reachable"
    category="NETWORK"
    priority="INFO"
    subject_template="UP: {{ip}}"
    body_template="""Object reachable: {{ip}}"""
    class Vars:
        source=Var(required=True)
        activator=Var(required=True)
        probe=Var(required=True)
        type=Var(required=True)
        ip=Var(required=True)
