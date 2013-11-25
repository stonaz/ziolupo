//var app = app || {};
//
//$(function() {
//    
//    app.preparazioni = new app.PaginatedCollection();
//    app.categoriepreparazioni =new app.CategoriePreparazioniView(  );
//   app.preparazioniView=new app.PreparazioniView({el: $('#Main')});
//  
//    
//    //alert('done')
//});

(function(){

	window.app = {};
	app.collections = {};
	app.models = {};
	app.views = {};
	app.mixins = {};

	// Defer initialization until doc ready.
	$(function(){
			app.collections.preparazioni = new app.collections.PaginatedCollection();
                        //app.collections.preparazioni.model=app.models.Item
			app.collections.categoriepreparazioni =new app.CategoriePreparazioniView(  );
                        app.views.preparazioniView=new app.PreparazioniView({el: $('#Main')});
                        app.views.preparazioni = new app.views.AppView({collection: app.collections.preparazioni});
			app.views.pagination = new app.views.PaginationView({collection:app.collections.preparazioni});
	});

})();
