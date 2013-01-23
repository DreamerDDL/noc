//---------------------------------------------------------------------
// NOC.main.ref.stencil.LookupField
//---------------------------------------------------------------------
// Copyright (C) 2007-2013 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.main.pyrule.LookupField");

Ext.define("NOC.main.ref.stencil.LookupField", {
    extend: "NOC.core.LookupField",
    alias: "widget.main.ref.stencil.LookupField",
    requires: ["NOC.main.ref.stencil.Lookup"]
});
