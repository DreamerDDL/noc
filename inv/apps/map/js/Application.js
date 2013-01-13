//---------------------------------------------------------------------
// inv.map application
//---------------------------------------------------------------------
// Copyright (C) 2007-2013 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.map.Application");

Ext.define("NOC.inv.map.Application", {
    extend: "NOC.core.Application",
    requires: [
        "NOC.inv.networkchart.LookupField",
        "NOC.inv.map.templates.ManagedObjectTooltip"
    ],
    // Label position style
    labelPositionStyle: {
        "nw": "verticalLabelPosition=top;verticalAlign=bottom;labelPosition=left;align=right",
        "n": "verticalLabelPosition=top;verticalAlign=bottom",
        "ne": "verticalLabelPosition=top;verticalAlign=bottom;labelPosition=right;align=left",
        "e": "labelPosition=right;align=left",
        "se": "verticalLabelPosition=bottom;verticalAlign=top;labelPosition=right;align=left",
        "s": "verticalLabelPosition=bottom;verticalAlign=top",
        sw: "verticalLabelPosition=bottom;verticalAlign=top;labelPosition=left;align=right",
        w: "labelPosition=left;align=right"
    },
    initComponent: function() {
        var me = this;
        me.chartCombo = Ext.create("NOC.inv.networkchart.LookupField", {
            fieldLabel: "Chart",
            labelWidth: 30,
            name: "chart",
            allowBlank: true,
            disabled: true,
            listeners: {
                scope: me,
                select: me.onSelectChart
            }
        });
        me.saveButton = Ext.create("Ext.button.Button", {
            iconCls: "icon_disk",
            text: "Save",
            tooltip: "Save changes",
            disabled: true,
            scope: me,
            handler: me.onSave
        });
        me.zoomInButton = Ext.create("Ext.button.Button", {
            tooltip: "Zoom In",
            iconCls: "icon_magnifier_zoom_in",
            scope: me,
            handler: me.onZoomIn,
            disabled: true
        });
        me.zoomOutButton = Ext.create("Ext.button.Button", {
            tooltip: "Zoom Out",
            iconCls: "icon_magifier_zoom_out",
            scope: me,
            handler: me.onZoomOut,
            disabled: true
        });
        me.zoomActualButton = Ext.create("Ext.button.Button", {
            tooltip: "Zoom Actual",
            iconCls: "icon_magnifier",
            scope: me,
            handler: me.onZoomActual,
            disabled: true
        });
        Ext.apply(me, {
            dockedItems: [{
                xtype: "toolbar",
                dock: "top",
                items: [
                    me.chartCombo,
                    "-",
                    // Editing
                    me.saveButton,
                    "-",
                    // Zoom
                    me.zoomInButton,
                    me.zoomOutButton,
                    me.zoomActualButton
                ]
            }],
            items: [{
                xtype: "component",
                autoScroll: true,
                style: {
                    background: "url('/static/img/grid.gif')"
                }
            }]
        });
        me.graph = undefined;
        // Context menus
        me.nodeContextMenu = Ext.create("Ext.menu.Menu", {
            items: [
                {
                    text: "Label Position",
                    menu: {
                        items: [
                            {
                                text: "Top Left",
                                iconCls: "icon_arrow_nw"
                            },
                            {
                                text: "Top",
                                iconCls: "icon_arrow_up"
                            },
                            {
                                text: "Top Right",
                                iconCls: "icon_arrow_ne"
                            },
                            {
                                text: "Right",
                                iconCls: "icon_arrow_right"
                            },
                            {
                                text: "Bottom Right",
                                iconCls: "icon_arrow_se"
                            },
                            {
                                text: "Bottom",
                                iconCls: "icon_arrow_down"
                            },
                            {
                                text: "Bottom Left",
                                iconCls: "icon_arrow_sw"
                            },
                            {
                                text: "Left",
                                iconCls: "icon_arrow_left"
                            }
                        ]
                    }
                }
            ]
        });
        me.callParent();
    },
    //
    afterRender: function() {
        var me = this;
        me.callParent();
        // Load mxGraph JS library
        mxLanguage = "en";
        mxLoadStylesheets = false;  // window scope
        mxImageBasePath = "/static/img/mxgraph/";
        mxLoadResources = false;
        load_scripts(["/static/js/mxClient.min.js"], me,
            me.onLoadJS);
    },
    //
    onLoadJS: function() {
        var me = this;
        me.chartCombo.setDisabled(false);
    },
    //
    onSelectChart: function(combo, records, opts) {
        var me = this;
        me.mapId = records[0].get("id");
        Ext.Ajax.request({
            url: "/inv/map/chart/" + me.mapId + "/",
            method: "GET",
            scope: me,
            success: me.loadChart
        });
    },
    // Initialize mxGraph
    initGraph: function() {
        var me = this;
        me.changeLog = [];
        me.saveButton.setDisabled(true);
        if(me.graph) {
            // Clear graph
            me.graph.removeCells(me.graph.getChildVertices(me.graph.getDefaultParent()), true);
        } else {
            // Create Graph
            var c = me.items.first().el.dom;
            mxEvent.disableContextMenu(c); // Disable default context menu
            me.graph = new mxGraph(c);
            me.graph.disconnectOnMove = false;
            // me.graph.foldingEnabled = false;
            me.graph.cellsResizable = false;
            new mxRubberband(me.graph);
            me.graph.setPanning(true);
            me.graph.setTooltips(true);
            // Set styles
            var ss = me.graph.getStylesheet(),
                edgeStyle = ss.getDefaultEdgeStyle();
            edgeStyle[mxConstants.STYLE_EDGE] = mxEdgeStyle.ElbowConnector;
            delete edgeStyle.endArrow;
            /*
            var vertexStyle = ss.getDefaultVertexStyle();
            vertexStyle[mxConstants.STYLE_FILLCOLOR] = "red";
            vertexStyle[mxConstants.STYLE_STROKECOLOR] = "blue";
            */
            // Load stencils
            var req = mxUtils.load("/static/shape/stencils.xml");
            var sroot = req.getDocumentElement();
            var shape = sroot.firstChild;
            while(shape != null) {
                if(shape.nodeType == mxConstants.NODETYPE_ELEMENT) {
                    mxStencilRegistry.addStencil(shape.getAttribute("name"),
                        new mxStencil(shape));
                }
                shape = shape.nextSibling;
            }
            // Inititalize tooltips
            me.graph.getTooltipForCell = me.getTooltipForCell;
            //
            me.graph.panningHandler.factoryMethod = Ext.bind(me.onContextMenu, me);
            // Add Event Handlers
            me.graph.addListener(mxEvent.MOVE_CELLS,
                Ext.bind(me.onNodeMove, me));
            //
            me.zoomInButton.setDisabled(false);
            me.zoomOutButton.setDisabled(false);
            me.zoomActualButton.setDisabled(false);
        }
    },
    //
    loadChart: function(response) {
        var me = this,
            data = Ext.decode(response.responseText);
        me.initGraph();
        me.graph.getModel().beginUpdate();
        try {
            // Update data
            var parent = me.graph.getDefaultParent(),
                nodes = {},  // id -> node
                ports = {};  // id -> port
            for(var i in data) {
                var n = data[i];
                switch(n.type) {
                    // Insert node
                    case "node":
                        var style = [];
                        // Label position
                        if(n.label) {
                            // Convert label position to style
                            var lp = n.label_position ? n.label_position : "s";
                            style.push(me.labelPositionStyle[lp]);
                        }
                        // Shape
                        if(n.shape) {
                            style.push("shape=" + n.shape);
                        }
                        // Draw node
                        var v = me.graph.insertVertex(parent, null,
                            n.label ? n.label : null,
                            n.x, n.y, n.w, n.h,
                            style ? style.join(";") : null
                        );
                        v.objectId = n.id;
                        // Attach tooltip
                        v.nocTooltipTemplate = me.templates.ManagedObjectTooltip;
                        v.nocTooltipData = {
                            name: n.label,
                            address: n.address,
                            platform: n.platform,
                            version: n.version
                        };
                        // Save id
                        if(n.id) {
                            nodes[n.id] = v;
                        };
                        // Create ports
                        for(var pi in n.ports) {
                            var pdata = n.ports[pi];
                            var pv = me.graph.insertVertex(v, null,
                                pdata.label, 1, 1, 5 * pdata.label.length, 12);
                            pv.geometry.offset = new mxPoint(3, 14 * pi - n.h);
                            pv.geometry.relative = true;
                            ports[pdata.id] = pv;
                        }
                        // End of node processing
                        break;
                    // Insert link
                    case "link":
                        var v = me.graph.insertEdge(parent, null, "",
                            ports[n.ports[0]], ports[n.ports[1]]);
                        break;
                }
            }
        }
        finally {
            // Update display
            me.graph.getModel().endUpdate();
        }
    },
    //
    getTooltipForCell: function(cell) {
        if(!cell.nocTooltipTemplate) {
            return "";
        }
        return cell.nocTooltipTemplate(cell.nocTooltipData);
    },
    // Save button pressed
    onSave: function() {
        var me = this;
        console.log(me.changeLog);
        Ext.Ajax.request({
            url: "/inv/map/chart/" + me.mapId + "/",
            method: "POST",
            jsonData: me.changeLog,
            scope: me,
            success: function() {
                me.changeLog = [];
                me.saveButton.setDisabled(true);
            }
        });
    },
    //
    registerChange: function(opts) {
        var me = this;
        me.changeLog.push(opts);
        me.saveButton.setDisabled(false);
    },
    // Register cell movement
    onNodeMove: function(graph, event) {
        var me = this;
        for(var i in event.properties.cells) {
            var c = event.properties.cells[i];
            if(c.vertex) {
                // Node moved
                console.log(c);
                me.registerChange({
                    cmd: "move",
                    type: "mo",
                    id: c.objectId,
                    x: c.geometry.x,
                    y: c.geometry.y,
                    w: c.geometry.width,
                    h: c.geometry.height
                });
            }
        }
    },
    // Zoom In
    onZoomIn: function() {
        var me = this;
        me.graph.zoomIn();
    },
    // Zoom Out
    onZoomOut: function() {
        var me = this;
        me.graph.zoomOut();
    },
    // Zoom Actual
    onZoomActual: function() {
        var me = this;
        me.graph.zoomActual();
    },
    //
    onContextMenu: function(menu, cell, evt) {
        var me = this;
        if(cell != null) {
            console.log(evt);
            me.nodeContextMenu.show();
        }
    }
});
