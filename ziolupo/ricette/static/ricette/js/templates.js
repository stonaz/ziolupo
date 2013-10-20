//Templates

var templateListeVeloci="\
<% for (var index = 0; index < liste.length; index++){ %>\
<% var lista = liste[index]; %>\
<li><a onclick=getLista(<%= lista.id %>)><%= lista.nome %></a></li>\
<% } %>\
";

        
var templateRicette="\
<% for (var index = 0; index < recipes.length; index++){ %>\
<% var recipe = recipes[index]; %>\
<div class='recipe'>\
<img src='media/<%= recipe.image %>' width='100' height='75' style='float: left;margin-right: 10px;'>\
<a href='#' onClick=showRecipe('<%= recipe.details %>')><%= recipe.nome %></a>\
<p class='spec'> <strong>Difficoltà: </strong><%= recipe.difficulty %></p>\
<p class='spec'><strong>Costo: </strong><%= recipe.costo %></p>\
<p class='spec'><strong>Tempo di preparazione: </strong><%= recipe.time %></p>\
</div>\
<% } %>\
";

var templateRicetta="\
<div >\
<h1><%= recipe.nome %></h1>\
<img src='media/<%= recipe.image %>' width='200' height='150' style='float: left;margin-right: 10px;'>\
<p > <strong>Difficoltà: </strong><%= recipe.difficulty %></p>\
<p ><strong>Costo: </strong><%= recipe.costo %></p>\
<p ><strong>Tempo di preparazione: </strong><%= recipe.time %></p>\
<\div>\
<div style='clear:left;padding-top:20px;';>\
<div class='testo' >\
<p ><strong>Ingredienti: </strong><br><%= recipe.ingredients %></p>\
</div>\
<div class='testo' >\
<strong>Preparazione: </strong><br><%= recipe.preparation %>\
</div>\
</div>\
 ";

var templateCounter="\
<br>\
<span class='counter' >Ricette trovate: <strong><%= count %></strong></span>\
 ";