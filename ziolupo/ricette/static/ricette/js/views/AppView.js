(function ( views ) {

	views.AppView = Backbone.View.extend({

		el : '#Main',

		initialize : function () {

			var tags = this.collection;

			tags.on('reset', this.addAll, this);
			tags.on('all', this.render, this);
			
			 console.log('received')
                  
//                  tags.fetch({
//				
//                                success: function(){
//					tags.pager();
//				},
//				error: function(response){
//					console.log(response)
//				},
//				silent:true
//			});

		},
		addAll : function () {
			this.$el.empty();
			this.collection.each (this.addOne);
		},
		
		addOne : function ( item ) {
			var view = new views.ResultView({model:item});
			$('#Main').append(view.render().el);
		},

		print: function(){
                 console.log('bye')
                 var tags = this.collection;
                 console.log(tags)
                 tags.fetch({
				
                                success: function(){
					tags.pager();
				},
				error: function(response){
					console.log(response)
				},
				silent:true
			});

		}
	});

})( app.views );
