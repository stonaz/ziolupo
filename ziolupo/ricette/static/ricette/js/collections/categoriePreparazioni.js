var app = app || {};

app.CategoriePreparazioni = Backbone.Collection.extend({
    model: app.CategoriaPreparazioni,
    url: '/categorie_preparazioni'  ,
    initialize: function() {
console.log('collection initialized')
},
});