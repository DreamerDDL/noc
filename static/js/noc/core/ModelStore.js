//---------------------------------------------------------------------
// NOC.core.ModelStore
//---------------------------------------------------------------------
// Copyright (C) 2007-2012 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.core.ModelStore");

Ext.define("NOC.core.ModelStore", {
    extend: "Ext.data.Store",
    filterParams: undefined,
    url: undefined,
    model: undefined,
    remoteSort: true,
    remoteFilter: true,
    customFields: [],

    constructor: function(config) {
        var me = this,
            model = Ext.create(config.model),
            fields = model.fields.items.concat(config.customFields),
            defaultValues = {};

        for(var i=0; i < fields.length; i++) {
            var field = fields[i],
                dv = field.defaultValue;
            if(dv != undefined) {
                defaultValues[field.name] = dv;
            }
        }
        // Additional fields
        fields = fields.concat([
            {
                name: "fav_status",
                type: "boolean",
                persist: false
            }
        ]);

        Ext.apply(config, {
            // model: config.model,
            model: null,
            fields: fields,  // Removed by superclass constructor
            defaultValues: defaultValues,
            implicitModel: true,
            proxy: Ext.create("Ext.data.RestProxy", {
                url: model.rest_url,
                pageParam: "__page",
                startParam: "__start",
                limitParam: "__limit",
                sortParam: "__sort",
                extraParams: {
                    "__format": "ext"
                },
                reader: {
                    type: "json",
                    root: "data",
                    totalProperty: "total",
                    successProperty: "success"
                },
                writer: {
                    type: "json"
                },
                listeners: {
                    exception: {
                        scope: me,
                        fn: me.onSyncException
                    }
                }
            }),
            listeners: {
                write: {
                    scope: me,
                    fn: me.onSyncWrite
                }
            },
            syncConfig: {}
        });
        //me.syncConfig = {};
        me.callParent([config]);
    },

    setFilterParams: function(config) {
        var me = this;
        me.filterParams = Ext.Object.merge({}, config);
        // Forcefully go to first page
        me.currentPage = 1;
    },

    load: function(config) {
        var me = this;
        config = Ext.Object.merge({
                params: Ext.Object.merge({}, me.filterParams)
            }, config);
        // Override callback
        // @todo: Call original callback
        config = Ext.Object.merge(config, {
            callback: function(records, operation, success) {
                if(!success)
                    NOC.error("Failed to fetch data!");
            }
        });
        // Continue loading
        me.callParent([config]);
    },
    // override sync()
    sync: function(config) {
        var me = this,
            conf = config || {};
        me.syncConfig = Ext.Object.merge({}, conf);
        me.callParent();
    },
    onSyncWrite: function() {
        var me = this;
        Ext.callback(me.syncConfig.success,
            me.syncConfig.scope || me);
    },
    onSyncException: function(proxy, response, op, opts) {
        var me = this,
            status = Ext.decode(response.responseText);
        status.status = response.status;
        Ext.callback(me.syncConfig.failure,
            me.syncConfig.scope || me, [response, op, status]);
    }
});
