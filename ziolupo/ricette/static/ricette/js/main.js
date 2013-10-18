function createListeVeloci() {

var url=window.__BASEURL__+"listeveloci/";

     $.ajax({
        async: true, 
        url: url,
        dataType: 'json',
	success: function(response){
       var lista = _.template(templateListeVeloci, { liste : response } );
       $("#ListeVeloci").append(lista)
        }
    });
}

function getLista(id) {

var url=window.__BASEURL__+"listeveloci/"+id;

     $.ajax({
        async: true, 
        url: url,
        dataType: 'json',
	success: function(response){
       $("#Intestazione").html(response.nome);
       var recipesURL=window.__BASEURL__+"ricette/?lista="+id;
       $("#myCarousel").hide()
       getRecipes(recipesURL,1)
        }
    });
}

function getCategory(id) {

var url=window.__BASEURL__+"categorie/"+id;

     $.ajax({
        async: true, 
        url: url,
        dataType: 'json',
	success: function(response){

       var categoriaPortata=response.portata;
       var categoriaNome= response.nome;
       $("#Intestazione").html(categoriaPortata + ' - ' + categoriaNome);
       var recipesURL=window.__BASEURL__+"ricette/?category="+id;
       $("#myCarousel").hide()
       getRecipes(recipesURL)
        }
    });
}

function getRecipes(recipesURL)
{

    $.ajax({
        async: true, 
        url: recipesURL,
        dataType: 'json',
        success: function(response){
       
       printRecipes(response);
      
        }
        
    });
}

function printRecipes(data)
{
$("#Ricette").html('');
$("#Pages").html('');
var count = _.template(templateCounter, { count : data.length } );
$("#Intestazione").append(count);
var output = _.template(templateRicette, { recipes : data } );
$("#Ricette").append(output);
	$("div.holder").jPages({
	    containerID : "Ricette",
	    perPage: 5,
            midRange: 3
            
  	});
}

function getRecipe(recipeURL)
{

    $.ajax({
        async: true, 
        url: recipeURL,
        dataType: 'json',
        success: function(response){
       
       printRecipe(response);
      
        }
        
    });
}

function printRecipe(data)
{
var output = _.template(templateRicetta, { recipe : data } );
$("#displayRecipe").append(output)
}

function showRecipe(url){
$('#overlay').fadeIn('fast',function(){
            $('#displayRecipe').show();
	    $('#displayRecipe').html('<a class="boxclose"  id="boxclose"></a>');
	    $('#boxclose').bind("click",function(){
				       $('#displayRecipe').hide("fast",function(){
				       $('#overlay').fadeOut('fast');
				  });
		});
	    getRecipe(url)
});
}


 $(function() {
	
    $.ajaxSetup({

        error: function(jqXHR, exception) {
            if (jqXHR.status === 0) {
                alert('Not connect.\n Verify Network.');
            } else if (jqXHR.status == 404) {
                alert('Requested page not found. [404]');
            } else if (jqXHR.status == 500) {
                alert('Internal Server Error [500].');
            } else if (exception === 'parsererror') {
                alert('Requested JSON parse failed.');
            } else if (exception === 'timeout') {
                alert('Time out error.');
            } else if (exception === 'abort') {
                alert('Ajax request aborted.');
            } else {
                alert('Uncaught Error.\n' + jqXHR.responseText);
            }
        }
    });
});