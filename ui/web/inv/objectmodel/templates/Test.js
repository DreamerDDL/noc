!function(){var n=Handlebars.template,e=NOC.templates.inv_objectmodel=NOC.templates.inv_objectmodel||{};e.Test=n({1:function(n,e,a,l,t){var o,i,r=null!=e?e:{};return"    <tr>\n        <td>\n"+(null!=(o=a.each.call(r,null!=e?e.names:e,{name:"each",hash:{},fn:n.program(2,t,0),inverse:n.noop,data:t}))?o:"")+"        </td>\n        <td>"+n.escapeExpression((i=null!=(i=a.direction||(null!=e?e.direction:e))?i:a.helperMissing,"function"==typeof i?i.call(r,{name:"direction",hash:{},data:t}):i))+"</td>\n        <td>\n            <table>\n"+(null!=(o=a.each.call(r,null!=e?e.connections:e,{name:"each",hash:{},fn:n.program(4,t,0),inverse:n.noop,data:t}))?o:"")+"            </table>\n        </td>\n    </tr>\n"},2:function(n,e,a,l,t){var o,i=null!=e?e:{},r=a.helperMissing,s="function",c=n.escapeExpression;return"                <b>"+c((o=null!=(o=a.name||(null!=e?e.name:e))?o:r,typeof o===s?o.call(i,{name:"name",hash:{},data:t}):o))+"</b><br/><i>("+c((o=null!=(o=a.description||(null!=e?e.description:e))?o:r,typeof o===s?o.call(i,{name:"description",hash:{},data:t}):o))+")</i><br/>\n"},4:function(n,e,a,l,t){var o,i=null!=e?e:{},r=a.helperMissing,s="function",c=n.escapeExpression;return"                <tr>\n                    <td>\n                        <b>"+c((o=null!=(o=a.name||(null!=e?e.name:e))?o:r,typeof o===s?o.call(i,{name:"name",hash:{},data:t}):o))+"</b><br/></i>("+c((o=null!=(o=a.description||(null!=e?e.description:e))?o:r,typeof o===s?o.call(i,{name:"description",hash:{},data:t}):o))+")</i>\n                    </td>\n                    <td><b>"+c((o=null!=(o=a.model||(null!=e?e.model:e))?o:r,typeof o===s?o.call(i,{name:"model",hash:{},data:t}):o))+"</b><br/>("+c((o=null!=(o=a.model_description||(null!=e?e.model_description:e))?o:r,typeof o===s?o.call(i,{name:"model_description",hash:{},data:t}):o))+")</td>\n                </tr>\n"},compiler:[7,">= 4.0.0"],main:function(n,e,a,l,t){var o,i,r=null!=e?e:{},s=a.helperMissing,c="function",d=n.escapeExpression;return"<h1>Possible connections for model "+d((i=null!=(i=a.name||(null!=e?e.name:e))?i:s,typeof i===c?i.call(r,{name:"name",hash:{},data:t}):i))+'</h1>\n<table border="1">\n'+(null!=(o=a.each.call(r,null!=e?e.connections:e,{name:"each",hash:{},fn:n.program(1,t,0),inverse:n.noop,data:t}))?o:"")+"</table>\n<h1>Internal crossing for "+d((i=null!=(i=a.name||(null!=e?e.name:e))?i:s,typeof i===c?i.call(r,{name:"name",hash:{},data:t}):i))+"</h1>\n"+d((a.grid||e&&e.grid||s).call(r,null!=e?e.crossing:e,{name:"grid",hash:{},data:t}))+"\n"},useData:!0})}();Ext.define("NOC.inv.objectmodel.templates.Test", {});