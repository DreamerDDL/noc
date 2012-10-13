//---------------------------------------------------------------------
// Application UI
//---------------------------------------------------------------------
// Copyright (C) 2007-2011 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC application");

Ext.application({
    name: "NOC",
    controllers: ["NOC.main.desktop.Controller"],

    launch: function() {
        var me = this;
        console.log("Initializing history API");
        Ext.History.init();
        console.log("NOC application starting");
        Ext.create("NOC.main.desktop.Viewport");
        console.log("NOC application ready");
        NOC.run = me.controllers.first().launchTab;
    }
});
