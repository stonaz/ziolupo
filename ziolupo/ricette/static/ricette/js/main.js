

function getCategory(id) {
/*
 * Load recipes
 */
//get category details:
var url="http://localhost/django/categorie/"+id;

     $.ajax({
        async: true, 
        url: url,
        dataType: 'json',
	success: function(response){

       var categoriaPortata=response.portata;
       var categoriaNome= response.nome;
       $("#Intestazione").html(categoriaPortata + ' - ' + categoriaNome);
       var recipesURL="http://localhost/django/ricette/?category="+id;
       $("#myCarousel").hide()
       getRecipes(recipesURL,1)
        }
    });

}

function getRecipes(recipesURL,start)
{

    $.ajax({
        async: true, 
        url: recipesURL,
        dataType: 'json',
        success: function(response){
       
       printRecipes(response,start);
      
        }
        
    });
}

function printRecipes(data,start)
{
 //var start=parseInt(start)
 //var offset=start - 1 + data.results.length;
 $("#Ricette").html('');
  $("#Pages").html('');
 //$("#Ricette").append('da ' + start +' a ' + offset + '<br>');
var count = _.template(templateCounter, { count : data.length } );
 $("#Intestazione").append(count);
 //$("#Intestazione").append('<br>Ricette trovate: ' + data.length);
 //if ( data.previous !==  null) {
 // //offsetPrev=offset - 3
 //  $("#Ricette").append('<button onClick=getRecipes(\''+ data.previous +'\',\''+ 1 +'\')> << </button>')
 //}
 //if ( data.next !== null) {
 // $("#Ricette").append('<button onClick=getRecipes(\''+ data.next +'\',\''+ 1 +'\')> >> </button>');
 //}
var output = _.template(templateRicette, { recipes : data } );
console.log(data.results)
$("#Ricette").append(output);

			var perPage = 3;
			var opened = 1;
			var onClass = 'on';
			var paginationSelector = '.pages';
$("#Ricette").simplePagination(perPage, 1, onClass, paginationSelector);
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
console.log(data.nome)
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