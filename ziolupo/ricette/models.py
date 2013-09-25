from django.db import models

# Create your models here.

class Portata(models.Model):
    nome = models.CharField("Portata", max_length=50)
    
    class Meta:
        app_label = 'ricette'
        verbose_name_plural = "Portate"
    
    def __unicode__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField("Categoria", max_length=50)
    slug = models.SlugField(null=True,max_length=100)
    portata = models.ForeignKey(Portata)
    
    class Meta:
        app_label = 'ricette'
        verbose_name_plural = "Categorie"
        
    #def save(self):
    #    # Place code here, which is excecuted the same
    #    # time the ``pre_save``-signal would be
    #    prefix = self.portata
    #    self.nome = "%s - %s" % (prefix, self.nome)
    #    # Call parent's ``save`` function
    #    super(Categoria, self).save()

        # Place code here, which is excecuted the same
        # time the ``post_save``-signal would be
    
    def __unicode__(self):
        return self.nome
    
    


class Ricetta(models.Model):
    nome = models.CharField("Nome",max_length=100)
    categoria = models.ForeignKey(Categoria)
    ingredients = models.TextField("Ingredienti")
    difficulty = models.CharField("Difficolta",max_length=100)
    preparation = models.TextField("Preparazione")
    costo= models.CharField("Costo",max_length=10)
    time = models.IntegerField("Tempo di preparazione")
    week_recipe = models.BooleanField("Ricetta della settimana",default=False)
    spotlight_recipe = models.BooleanField("Ricetta in rilievo",default=False)
    
    class Meta:
        app_label = 'ricette'
        verbose_name_plural = "Ricette"
    
    def __unicode__(self):
        return self.nome

    

    
    
