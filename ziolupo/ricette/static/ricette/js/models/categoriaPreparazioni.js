var app = app || {};

app.CategoriaPreparazioni = Backbone.Model.extend({
    defaults: {
    details: "",
    id: 1, 
    nome: "",
},
 initialize: function() {
console.log('model initialized')
},
});