//---------------------------------------------------------------------
// sa.managedobjectselector application
//---------------------------------------------------------------------
// Copyright (C) 2007-2014 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.sa.managedobjectselector.Application");

Ext.define("NOC.sa.managedobjectselector.Application", {
    extend: "NOC.core.ModelApplication",
    requires: [
        "NOC.sa.managedobjectselector.Model",
        "NOC.sa.managedobjectselector.AttributesModel",
        "NOC.sa.managedobjectselector.LookupField",
        "NOC.sa.managedobjectselector.M2MField",
        "NOC.sa.managedobjectprofile.LookupField",
        "NOC.main.prefixtable.LookupField",
        "NOC.sa.administrativedomain.LookupField",
        "NOC.ip.vrf.LookupField",
        "NOC.vc.vcdomain.LookupField",
        "NOC.sa.terminationgroup.LookupField",
        "NOC.sa.terminationgroup.LookupField",
        "NOC.main.ref.profile.LookupField"
    ],
    model: "NOC.sa.managedobjectselector.Model",
    search: true,

    initComponent: function() {
        var me = this;

        me.ITEM_OBJECTS = me.registerItem(
            "NOC.sa.managedobjectselector.ObjectsPanel"
        );
        me.objectsButton = Ext.create("Ext.button.Button", {
            text: __("Matched Objects"),
            glyph: NOC.glyph.list,
            scope: me,
            handler: me.onObjects
        });
        Ext.apply(me, {
            columns: [
                {
                    text: __("Name"),
                    dataIndex: "name",
                    width: 200
                },
                {
                    text: __("Enabled"),
                    dataIndex: "is_enabled",
                    width: 50,
                    renderer: NOC.render.Bool
                },
                {
                    text: __("Expression"),
                    dataIndex: "expression",
                    flex: 1
                }
            ],
            fields: [
                {
                    name: "name",
                    xtype: "textfield",
                    fieldLabel: __("Name"),
                    allowBlank: false,
                    uiStyle: "medium"
                },
                {
                    name: "description",
                    xtype: "textarea",
                    fieldLabel: __("Description"),
                    allowBlank: true
                },
                {
                    name: "is_enabled",
                    xtype: "checkboxfield",
                    boxLabel: __("Is Enabled"),
                    allowBlank: false
                },
                {
                    name: "filter_id",
                    xtype: "numberfield",
                    fieldLabel: __("Filter by ID"),
                    allowBlank: true,
                    uiStyle: "small",
                    hideTrigger: true
                },
                {
                    name: "filter_name",
                    xtype: "textfield",
                    fieldLabel: __("Filter by Name (REGEXP)"),
                    allowBlank: true,
                    uiStyle: "large"
                },
                {
                    name: "filter_managed",
                    xtype: "combobox",
                    fieldLabel: __("Filter by Is Managed"),
                    allowBlank: true,
                    store: [
                        [null, "-"],
                        [true, "Yes"],
                        [false, "No"]
                    ],
                    uiStyle: "small"
                },
                {
                    name: "filter_profile",
                    xtype: "main.ref.profile.LookupField",
                    fieldLabel: __("Filter by Profile"),
                    allowBlank: true
                },
                {
                    name: "filter_object_profile",
                    xtype: "sa.managedobjectprofile.LookupField",
                    fieldLabel: __("Filter by Object Profile"),
                    allowBlank: true
                },
                {
                    name: "filter_address",
                    xtype: "textfield",
                    fieldLabel: __("Filter by Address (REGEXP)"),
                    allowBlank: true
                },
                {
                    name: "filter_prefix",
                    xtype: "main.prefixtable.LookupField",
                    fieldLabel: __("Filter by Prefix Table"),
                    allowBlank: true
                },
                {
                    name: "filter_administrative_domain",
                    xtype: "sa.administrativedomain.LookupField",
                    fieldLabel: __("Filter by Administrative Domain"),
                    allowBlank: true
                },
                {
                    name: "filter_vrf",
                    xtype: "ip.vrf.LookupField",
                    fieldLabel: __("Filter by VRF"),
                    allowBlank: true
                },
                {
                    name: "filter_vc_domain",
                    xtype: "vc.vcdomain.LookupField",
                    fieldLabel: __("Filter by VC Domain"),
                    allowBlank: true
                },
                {
                    name: "filter_termination_group",
                    xtype: "sa.terminationgroup.LookupField",
                    fieldLabel: __("Filter by termination group"),
                    allowBlank: true
                },
                {
                    name: "filter_service_terminator",
                    xtype: "sa.terminationgroup.LookupField",
                    fieldLabel: __("Filter by service terminator"),
                    allowBlank: true
                },
                {
                    name: "filter_user",
                    xtype: "textfield",
                    fieldLabel: __("Filter by User (REGEXP)"),
                    allowBlank: true
                },
                {
                    name: "filter_remote_path",
                    xtype: "textfield",
                    fieldLabel: __("Filter by Remote Path (REGEXP)"),
                    allowBlank: true
                },
                {
                    name: "filter_description",
                    xtype: "textfield",
                    fieldLabel: __("Filter by Description (REGEXP)"),
                    allowBlank: true
                },
                {
                    name: "filter_tags",
                    xtype: "textfield",
                    fieldLabel: __("Filter By Tags"),
                    allowBlank: true
                },
                {
                    name: "source_combine_method",
                    xtype: "combobox",
                    fieldLabel: __("Source Combine Method"),
                    allowBlank: false,
                    store: [
                        ["O", "OR"],
                        ["A", "AND"]
                    ],
                    uiStyle: "small"
                },
                {
                    xtype: "sa.managedobjectselector.M2MField",
                    name: "sources",
                    height: 220,
                    width: 600,
                    fieldLabel: __("Sources"),
                    buttons: ["add", "remove"],
                    allowBlank: true
                }
            ],
            inlines: [
                {
                    title: "Filter by attributes",
                    model: "NOC.sa.managedobjectselector.AttributesModel",
                    columns: [
                        {
                            text: __("Key (RE)"),
                            dataIndex: "key_re",
                            width: 100,
                            editor: "textfield"
                        },
                        {
                            text: __("Value (RE)"),
                            dataIndex: "value_re",
                            editor: "textfield",
                            flex: 1
                        }
                    ]
                }
            ],
            formToolbar: [
                me.objectsButton
            ]
        });
        me.callParent();
    },
    //
    onObjects: function() {
        var me = this;
        me.previewItem(me.ITEM_OBJECTS, me.currentRecord);
    }
});