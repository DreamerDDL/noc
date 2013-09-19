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
        Ext.create("Ext.Viewport", {
            layout: "border",
            items: [
                Ext.create("NOC.main.desktop.HeaderPanel"),
                Ext.create("NOC.main.desktop.NavPanel"),
                Ext.create("NOC.main.desktop.WorkplacePanel")
            ]
        });
        console.log("NOC application ready");
        var controller = me.controllers.first();
        NOC.run = controller.launchTab;
        NOC.launch = Ext.bind(controller.launchApp, controller);
        //
        var h = Ext.History.getHash();
        if(h) {
            // Open application tab
            var p = h.split("/"),
                app = p[0],
                args = p.slice(1);
            if(args.length > 0) {
                NOC.launch(app, "history", {args: args});
            } else {
                NOC.launch(app);
            }
        }
    }
});
