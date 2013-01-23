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
        "NOC.inv.map.templates.ManagedObjectTooltip",
        "NOC.inv.map.templates.LinkTooltip",
        "NOC.inv.map.templates.InterfaceTooltip"
    ],
    // Label position style
    labelPositionStyle: {
        nw: "verticalLabelPosition=top;verticalAlign=bottom;labelPosition=left;align=right",
        n: "verticalLabelPosition=top;verticalAlign=bottom",
        ne: "verticalLabelPosition=top;verticalAlign=bottom;labelPosition=right;align=left",
        e: "labelPosition=right;align=left",
        se: "verticalLabelPosition=bottom;verticalAlign=top;labelPosition=right;align=left",
        s: "verticalLabelPosition=bottom;verticalAlign=top",
        sw: "verticalLabelPosition=bottom;verticalAlign=top;labelPosition=left;align=right",
        w: "labelPosition=left;align=right"
    },
    edgeStyle: {
        straight: "",
        orthogonal: "edgeStyle=elbowEdgeStyle"
    },
    NS_NORMAL: "n",
    NS_WARNING: "w",
    NS_ALARM: "a",
    NS_UNREACH: "u",

    initComponent: function() {
        var me = this;
        me.chartCombo = Ext.create("NOC.inv.networkchart.LookupField", {
            fieldLabel: "Chart",
            labelWidth: 30,
            name: "chart",
            allowBlank: true,
            disabled: true,
            emptyText: "Select chart...",
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
        me.reloadButton = Ext.create("Ext.button.Button", {
            iconCls: "icon_arrow_refresh",
            text: "Reload",
            tooltip: "Reload map",
            disabled: true,
            scope: me,
            handler: me.onReload
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
                    me.reloadButton,
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
                    text: "Fold",
                    listeners: {
                        scope: me,
                        click: me.onFold
                    }
                },
                {
                    text: "Unfold",
                    listeners: {
                        scope: me,
                        click: me.onUnfold
                    }
                },
                {
                    text: "Label Position",
                    menu: {
                        items: [
                            {
                                text: "Top Left",
                                iconCls: "icon_arrow_nw",
                                itemId: "nw",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Top",
                                iconCls: "icon_arrow_up",
                                itemId: "n",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Top Right",
                                iconCls: "icon_arrow_ne",
                                itemId: "ne",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Right",
                                iconCls: "icon_arrow_right",
                                itemId: "e",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Bottom Right",
                                iconCls: "icon_arrow_se",
                                itemId: "se",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Bottom",
                                iconCls: "icon_arrow_down",
                                itemId: "s",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Bottom Left",
                                iconCls: "icon_arrow_sw",
                                itemId: "sw",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            },
                            {
                                text: "Left",
                                iconCls: "icon_arrow_left",
                                itemId: "w",
                                listeners: {
                                    scope: me,
                                    click: me.onLabelPositionChange
                                }
                            }
                        ]
                    }
                },
                {
                    text: "Select Icon ...",
                    listeners: {
                        scope: me,
                        click: me.onSelectIcon
                    }
                }
            ]
        });
        me.edgeContextMenu = Ext.create("Ext.menu.Menu", {
            items: [
                {
                    text: "Line Style",
                    menu: {
                        items: [
                            {
                                text: "Staight",
                                itemId: "straight",
                                listeners: {
                                    scope: me,
                                    click: me.onEdgeStyleChange
                                }
                            },
                            {
                                text: "Orthogonal",
                                itemId: "orthogonal",
                                listeners: {
                                    scope: me,
                                    click: me.onEdgeStyleChange
                                }
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
        me.requestChart();
    },
    //
    requestChart: function() {
        var me = this;
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
        me.reloadButton.setDisabled(true);
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
            me.graph.foldingEnabled = false;
            // Set styles
            var ss = me.graph.getStylesheet(),
                edgeStyle = ss.getDefaultEdgeStyle();
            // edgeStyle[mxConstants.STYLE_EDGE] = mxEdgeStyle.ElbowConnector;
            delete edgeStyle.endArrow;
            /*
            var vertexStyle = ss.getDefaultVertexStyle();
            vertexStyle[mxConstants.STYLE_FILLCOLOR] = "red";
            vertexStyle[mxConstants.STYLE_STROKECOLOR] = "blue";
            */
            // Load stencils
            var req = mxUtils.load("/inv/map/stencils/");
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
        var model = me.graph.getModel();
        model.beginUpdate();
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
                        if(n.collapsed) {
                            model.setCollapsed(v, true);
                        }
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
                            // Tooltips
                            pv.nocTooltipTemplate = me.templates.InterfaceTooltip;
                            pv.nocTooltipData = {
                                interface: pdata.label
                            }
                        }
                        // Set initial status
                        me.setNodeStatus(v, n.status);
                        // End of node processing
                        break;
                    // Insert link
                    case "link":
                        var style = [];
                        // Adjust edge style
                        if(n.edge_style && n.edge_style != "straight") {
                            style.push(me.edgeStyle[n.edge_style]);
                        }
                        // Create edge
                        var v = me.graph.insertEdge(parent, null, "",
                            ports[n.ports[0]], ports[n.ports[1]],
                            style ? style.join(";") : null
                        );
                        v.objectId = n.id;
                        // Tooltips
                        v.nocTooltipTemplate = me.templates.LinkTooltip;
                        v.nocTooltipData = {
                            discovery_method: n.discovery_method
                        };
                        break;
                }
            }
        }
        finally {
            // Update display
            model.endUpdate();
        }
        me.reloadButton.setDisabled(false);
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
    onReload: function() {
        var me = this;
        me.requestChart();
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
            var m = null;
            console.log(evt);
            if(cell.isVertex()) {
                m = me.nodeContextMenu;
            } else {
                m = me.edgeContextMenu;
            }
            if(m) {
                m.setPosition(evt.pageX, evt.pageY);
                m.show();
            }
        }
    },
    //
    onLabelPositionChange: function(item, event, opt) {
        var me = this,
            selection = me.graph.getSelectionCells(),
            model = me.graph.getModel(),
            ls = me.labelPositionStyle[item.itemId].split(";");
        model.beginUpdate();
        for(var i in selection) {
            var c = selection[i];
            if(c.isVertex()) {
                me.registerChange({
                    cmd: "label_position",
                    type: "mo",
                    id: c.objectId,
                    label_position: item.itemId
                });
                // Reset styles
                me.graph.setCellStyles("verticalLabelPosition", null, [c]);
                me.graph.setCellStyles("verticalAlign", null, [c]);
                me.graph.setCellStyles("labelPosition", null, [c]);
                me.graph.setCellStyles("align", null, [c]);
                // Dynamically apply styles
                for(var j in ls) {
                    var ss = ls[j].split("=");
                    me.graph.setCellStyles(ss[0], ss[1], [c]);
                }
            }
        }
        model.endUpdate();
    },
    //
    setSelectionCollapsed: function(collapsed) {
        var me = this,
            selection = me.graph.getSelectionCells(),
            model = me.graph.getModel();
        model.beginUpdate()
        for(var i in selection) {
            var c = selection[i];
            if(c.isVertex() && c.isCollapsed() != collapsed) {
                model.setCollapsed(c, collapsed);
                me.registerChange({
                    cmd: "collapsed",
                    type: "mo",
                    id: c.objectId,
                    collapsed: collapsed
                });
            }
        }
        model.endUpdate()
    },
    //
    onFold: function(item, event, opt) {
        var me = this;
        me.setSelectionCollapsed(true);
    },
    //
    onUnfold: function(item, event, opt) {
        var me = this;
        me.setSelectionCollapsed(false);
    },
    //
    onEdgeStyleChange: function(item, event, opt) {
        var me = this,
            selection = me.graph.getSelectionCells(),
            model = me.graph.getModel();
        model.beginUpdate();
        for(var i in selection) {
            var c = selection[i];
            if(c.isEdge()) {
                me.registerChange({
                    cmd: "edge_style",
                    type: "link",
                    id: c.objectId,
                    edge_style: item.itemId
                });
                var es = {
                    straight: null,
                    orthogonal: "elbowEdgeStyle"
                }[item.itemId];
                me.graph.setCellStyles(mxConstants.STYLE_EDGE, es, [c]);
            }
        }
        model.endUpdate();
    },
    //
    onSelectIcon: function() {
        var me = this;
        Ext.create("NOC.inv.map.SelectIconForm", {app: me});
    },
    //
    setIcon: function(shape) {
        var me = this,
            selection = me.graph.getSelectionCells(),
            model = me.graph.getModel();
        model.beginUpdate();
        for(var i in selection) {
            var c = selection[i];
            if(c.isVertex()) {
                me.registerChange({
                    cmd: "shape",
                    type: "mo",
                    id: c.objectId,
                    shape: shape
                });
                me.graph.setCellStyles(
                    mxConstants.STYLE_SHAPE, shape, [c]);
            }
        }
        model.endUpdate();
    },
    // Manipulate cell overlays
    setCellOverlay: function(cell, img, tooltip) {
        var me = this,
            overlay = new mxCellOverlay(img, tooltip);
        overlay.addListener(mxEvent.CLICK, function(sender, evt) {});
        me.removeCellOverlays(cell);
        me.graph.addCellOverlay(cell, overlay);
    },
    removeCellOverlays: function(cell) {
        var me = this;
        me.graph.removeCellOverlays(cell);
    },
    //
    setNodeStatus: function(cell, status) {
        var me = this;
        if(cell.nocStatus == status) {
            return;
        }
        if(status == me.NS_NORMAL) {
            me.removeCellOverlays(cell);
        } else {
            me.setCellOverlay(cell, me.graph.warningImage, status);
        }
        cell.nocStatus = status;
    }
});
