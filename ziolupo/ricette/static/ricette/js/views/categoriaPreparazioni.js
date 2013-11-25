var app = app || {};

app.CategoriaPreparazioniView = Backbone.View.extend({
    events: {
'click li': 'test',
},


test: function() {
console.log(this.model.get('id'));
app.views.preparazioni.print();

},   
    template: _.template( $( '#tmplCategoriaPreparazioni' ).html() ),

    render: function() {
        //this.el is what we defined in tagName. use $el to get access to jQuery html() function
        this.$el.html( this.template( this.model.toJSON() ) );

        return this;
    },
    
});