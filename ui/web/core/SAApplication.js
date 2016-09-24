//---------------------------------------------------------------------
// NOC.core.SAApplication
//---------------------------------------------------------------------
// Copyright (C) 2007-2016 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.core.SAApplication");

Ext.define("NOC.core.SAApplication", {
    extend: "NOC.core.Application",
    layout: "card",
    storeFields: [
        "id", "name", "address", "profile_name",
        "platform", "row_class", "status", "result"
    ],

    stateMap: {
        w: __("Waiting"),
        r: __("Running"),
        s: __("Success"),
        f: __("Failed")
    },

    initComponent: function() {
        var me = this,
            bs = 100;

        me.selectionStore = Ext.create("NOC.core.ModelStore", {
            model: "NOC.core.SAApplicationModel",
            autoLoad: true,
            pageSize: bs,
            leadingBufferZone: bs,
            numFromEdge: Math.ceil(bs / 2),
            trailingBufferZone: bs
        });
        me.store = Ext.create("Ext.data.Store", {
            fields: me.storeFields,
            listeners: {
                scope: me,
                add: me.onChangeSelection,
                remove: me.onChangeSelection
            }
        });
        me.ITEM_SELECT = me.registerItem(
            me.createSelectPanel()
        );
        me.ITEM_CONFIG = me.registerItem(
            me.createConfigPanel()
        );
        me.ITEM_PROGRESS = me.registerItem(
            me.createProgressPanel()
        );
        // me.ITEM_REPORT = me.registerItem(
        //     me.createReportPanel()
        // );
        Ext.apply(me, {
            items: me.getRegisteredItems(),
            activeItem: me.ITEM_SELECT
        });
        me.callParent();
    },
    //
    createSelectPanel: function() {
        var me = this,
            selectGrid, selectedGrid;

        selectGrid = Ext.create("Ext.grid.Panel", {
            store: me.selectionStore,
            flex: 1,
            border: false,
            autoScroll: true,
            stateful: true,
            stateId: me.appName + "-select-grid",
            plugins: [
                {
                    ptype: "bufferedrenderer"
                }
            ],
            selModel: "checkboxmodel",
            columns: [
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 150
                },
                {
                    text: __("Address"),
                    dataIndex: "address",
                    width: 70
                },
                {
                    text: __("Profile"),
                    dataIndex: "profile_name",
                    width: 100
                },
                {
                    text: __("Platform"),
                    dataIndex: "platform",
                    flex: 1
                },
                {
                    xtype: "glyphactioncolumn",
                    width: 25,
                    items: [
                        {
                            glyph: NOC.glyph.arrow_right,
                            scope: me,
                            handler: me.onAddObject
                        }
                    ]
                }
            ],
            dockedItems: [
                {
                    xtype: "toolbar",
                    dock: "top",
                    items: [
                        // @todo: Search
                        {
                            glyph: NOC.glyph.refresh
                        },
                        {
                            text: __("Select Checked"),
                            glyph: NOC.glyph.plus_circle,
                            disabled: true
                        },
                        {
                            text: __("Select All"),
                            glyph: NOC.glyph.plus_circle,
                            disabled: true
                        }
                    ]
                }
            ],
            viewConfig: {
                getRowClass: Ext.bind(me.getRowClass, me)
            }
        });

        selectedGrid = Ext.create("Ext.grid.Panel", {
            store: me.store,
            flex: 1,
            autoScroll: true,
            stateful: true,
            stateId: me.appName + "-selected-grid",
            selModel: "checkboxmodel",
            columns: [
                {
                    xtype: "glyphactioncolumn",
                    width: 25,
                    items: [
                        {
                            glyph: NOC.glyph.arrow_left,
                            scope: me,
                            handler: me.onRemoveObject
                        }
                    ]
                },
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 150
                },
                {
                    text: __("Address"),
                    dataIndex: "address",
                    width: 70
                },
                {
                    text: __("Profile"),
                    dataIndex: "profile_name",
                    width: 100
                },
                {
                    text: __("Platform"),
                    dataIndex: "platform",
                    flex: 1
                }
            ],
            dockedItems: [
                {
                    xtype: "toolbar",
                    dock: "top",
                    items: [
                        {
                            text: __("Remove Checked"),
                            glyph: NOC.glyph.minus_circle,
                            disabled: true
                        },
                        {
                            text: __("Remove All"),
                            glyph: NOC.glyph.minus_circle,
                            disabled: true
                        }
                    ]
                }
            ],
            viewConfig: {
                getRowClass: Ext.bind(me.getRowClass, me)
            }
        });

        me.selectedTotalField = Ext.create("Ext.form.field.Display", {
            value: __("Total") + ": " + 0
        });

        me.selectContinueButton = Ext.create("Ext.button.Button", {
            text: __("Continue"),
            glyph: NOC.glyph.play,
            disabled: true,
            handler: function() {
                me.showItem(me.ITEM_CONFIG);
            }
        });

        return Ext.create("Ext.panel.Panel", {
            layout: "hbox",
            items: [
                selectGrid,
                selectedGrid
            ],
            dockedItems: [
                {
                    xtype: "toolbar",
                    dock: "top",
                    items: [
                        me.selectContinueButton,
                        "->",
                        me.selectedTotalField
                    ]
                }
            ]
        });
    },
    //
    createConfigPanel: function() {
        var me = this,
            selectedGrid;

        selectedGrid = Ext.create("Ext.grid.Panel", {
            store: me.store,
            flex: 1,
            autoScroll: true,
            stateful: true,
            stateId: me.appName + "-selected-grid",
            columns: [
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 150
                },
                {
                    text: __("Address"),
                    dataIndex: "address",
                    width: 70
                },
                {
                    text: __("Profile"),
                    dataIndex: "profile_name",
                    width: 100
                },
                {
                    text: __("Platform"),
                    dataIndex: "platform",
                    flex: 1
                }
            ]
        });

        me.runButton = Ext.create("Ext.button.Button", {
            text: __("Run"),
            glyph: NOC.glyph.play,
            disabled: true,
            scope: me,
            handler: me.onRun
        });

        return Ext.create("Ext.panel.Panel", {
            layout: "hbox",
            items: [
                selectedGrid,
                me.getConfigPanel()
            ],
            dockedItems: [
                {
                    xtype: "toolbar",
                    dock: "top",
                    items: [
                        {
                            glyph: NOC.glyph.arrow_left,
                            scope: me,
                            tooltip: __("Back"),
                            handler: function() {
                                me.showItem(me.ITEM_SELECT);
                            }
                        },
                        "-",
                        me.runButton
                    ]
                }
            ]
        });
    },
    //
    createProgressPanel: function() {
        var me = this,
            selectedGrid;
        //
        me.progressState = {
            w: Ext.create({
                xtype: "button",
                text: __("Waiting"),
                enableToggle: true,
                pressed: true
            }),
            r: Ext.create({
                xtype: "button",
                text: __("Running"),
                enableToggle: true,
                pressed: true
            }),
            f: Ext.create({
                xtype: "button",
                text: __("Failed"),
                enableToggle: true,
                pressed: true
            }),
            s: Ext.create({
                xtype: "button",
                text: __("Success"),
                enableToggle: true,
                pressed: true
            })
        };

        selectedGrid = Ext.create("Ext.grid.Panel", {
            store: me.store,
            flex: 1,
            autoScroll: true,
            stateful: true,
            stateId: me.appName + "-selected-grid",
            columns: [
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 150
                },
                {
                    text: __("Address"),
                    dataIndex: "address",
                    width: 70
                },
                {
                    text: __("Profile"),
                    dataIndex: "profile_name",
                    width: 100
                },
                {
                    text: __("Platform"),
                    dataIndex: "platform",
                    flex: 1
                }
            ],
            listeners: {
                scope: me,
                select: me.onShowResult
            },
            dockedItems: [{
                xtype: "toolbar",
                dock: "top",
                items: [
                    me.progressState.w,
                    me.progressState.r,
                    me.progressState.s,
                    me.progressState.f
                ]
            }]
        });

        me.resultPanel = me.getResultPanel();

        return Ext.create("Ext.panel.Panel", {
            layout: "hbox",
            items: [
                selectedGrid,
                me.resultPanel
            ],
            dockedItems: [
                {
                    xtype: "toolbar",
                    dock: "top",
                    items: [
                        {
                            glyph: NOC.glyph.arrow_left,
                            tooltip: __("Back"),
                            disabled: true
                        },
                        {
                            glyph: NOC.glyph.print,
                            tooltip: __("Report"),
                            disabled: true
                        }
                    ]
                }
            ]
        });
    },
    //
    createReportPanel: function() {
        var me = this;
    },
    //
    getSelectionRowClass: function(record, index, params, store) {
        var me = this,
            c = record.get("row_class");
        if(c) {
            return c;
        } else {
            return "";
        }
    },
    // Return Grid's row classes
    getRowClass: function(record, index, params, store) {
        var me = this,
            c = record.get("row_class");
        if(c) {
            return c;
        } else {
            return "";
        }
    },
    //
    onAddObject: function(grid, rowIndex, colIndex) {
        var me = this,
            r = grid.store.getAt(rowIndex);
        if(!me.store.getById(r.get("id"))) {
            me.store.add(r);
        }
    },
    //
    onRemoveObject: function(grid, rowIndex, colIndex) {
        var me = this;
        grid.store.removeAt(rowIndex);
    },
    //
    onChangeSelection: function() {
        var me = this,
            count = me.store.getCount();
        me.selectedTotalField.setValue(__("Total") + ": " + count);
        me.selectContinueButton.setDisabled(!count);
    },
    //
    onRun: function() {
        var me = this;
        // check errors
        me.showItem(me.ITEM_PROGRESS);
        me.onUpdateProgress();
    },
    //
    onShowResult: function(grid, record) {
        var me = this;
        me.resultPanel.showResult(record.get("result"));
    },
    //
    onUpdateProgress: function() {
        var me = this,
            r = {w: 0, r: 0, s: 0, f: 0};
        me.store.each(function(record) {
            var s = record.get("state") || "w";
            r[s] += 1;
        });
        Ext.Object.each(function(k, v) {
            var b = me.progressState[k];
            // @todo: Set badge
        });
    }
});
