var app = app || {}

app.TestView = Backbone.View.extend({
el: $('#Main'),
// Cache the template function for a single item.
todoTpl: _.template( "An example template" ),
initialize:function() {
    //$('#Preparazioni').bind('click', this.print);
    //this.$el.html( 'oh' );
},
print: function() {
    console.log('i am listening');
    //console.log(this.$el)
   // this.$el.html( 'oh oh' );
    
}
});
