var app = app || {};

app.CategoriePreparazioniView = Backbone.View.extend({

el: '#Preparazioni',



initialize: function() {
this.collection = new app.CategoriePreparazioni();
this.collection.fetch({reset: true}); // NEW
//this.render();
this.listenTo( this.collection, 'add', this.renderCategoriaPreparazioni );
this.listenTo( this.collection, 'reset', this.render ); // NEW
},
    // render library by rendering each book in its collection
    render: function() {
        
        this.collection.each(function( item ) {
            //console.log(item)
            this.renderCategoriaPreparazioni( item );
        }, this );
       // console.log('rendering..')
    },

    // render a book by creating a BookView and appending the
    // element it renders to the library's element
    renderCategoriaPreparazioni: function( item ) {
        var categoriaPreparazioniView = new app.CategoriaPreparazioniView({
            model: item
        });
        this.$el.append( categoriaPreparazioniView.render().el );
    }
})