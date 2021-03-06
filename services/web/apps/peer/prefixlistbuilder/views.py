# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Interactive prefix list builder
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Django modules
from django import forms
from django.core.validators import RegexValidator
# NOC modules
from noc.lib.app.extapplication import ExtApplication, view
from noc.peer.models.peeringpoint import PeeringPoint
from noc.peer.models.whoiscache import WhoisCache
from noc.sa.interfaces.base import UnicodeParameter, ModelParameter
from noc.core.translation import ugettext as _

as_set_re = "^AS(?:\d+|-\S+)(:\S+)?(?:\s+AS(?:\d+|-\S+)(:\S+)?)*$"


class PrefixListBuilderForm(forms.Form):
    """
    Builder form
    """
    peering_point = forms.ModelChoiceField(
        queryset=PeeringPoint.objects.all())
    name = forms.CharField(required=False)
    as_set = forms.CharField(validators=[RegexValidator(as_set_re)])

    def clean(self):
        if not self.cleaned_data["name"] and "as_set" in self.cleaned_data:
            self.cleaned_data["name"] = self.cleaned_data["as_set"]
        return self.cleaned_data


class PrefixListBuilderApplication(ExtApplication):
    """
    Interactive prefix list builder
    """
    title = _("Prefix List Builder")
    menu = _("Prefix List Builder")

    @view(
        method=["GET"], url=r"^$", access="read", api=True,
        validate={
            "peering_point": ModelParameter(PeeringPoint),
            "name": UnicodeParameter(required=False),
            "as_set": UnicodeParameter()
        }
    )
    def api_list(self, request, peering_point, name, as_set):
        prefixes = WhoisCache.resolve_as_set_prefixes_maxlen(as_set)
        pl = peering_point.get_profile().generate_prefix_list(name, prefixes)
        return {
            "name": name,
            "prefix_list": pl,
            "success": True
        }
