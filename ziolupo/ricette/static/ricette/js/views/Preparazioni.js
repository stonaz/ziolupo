var app = app || {}

app.PreparazioniView = Backbone.View.extend({
el: $('#Main'),
// Cache the template function for a single item.
todoTpl: _.template( "An example template" ),
initialize:function() {
    //$('#Preparazioni').bind('click', this.print);
    //this.$el.html( 'oh' );
},
print: function(n) {
    console.log('i am listening and i heard' + n);
    //console.log(this.$el)
    this.$el.html( 'oh oh' );
    
}
});
