from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

PORTATE = (
        ('Antipasti', 'Antipasti'),
        ('Primi', 'Primi'),
        ('Secondi', 'Secondi'),
        ('Contorni', 'Contorni'),
        ('Dolci', 'Dolci'),
    )
    
class Categoria(models.Model):
    nome = models.CharField("Categoria", max_length=50, default= ' ')
    slug = models.SlugField(null=True,blank=True,max_length=100)
    portata = models.CharField("Tipologia", max_length=20,null=False,choices=PORTATE)
    
    class Meta:
        app_label = 'ricette'
        verbose_name_plural = "Categorie"
        ordering = ['nome']
    
    def __unicode__(self):
        return "%s - %s" % (self.portata, self.nome)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.nome)
        super(Categoria, self).save()
    
    


class Ricetta(models.Model):
    nome = models.CharField("Nome",max_length=100)
    slug = models.SlugField(null=True,blank=True,max_length=100)
    categoria = models.ForeignKey(Categoria,related_name='ricette')
    ingredients = models.TextField("Ingredienti")
    difficulty = models.CharField("Difficolta",max_length=100)
    preparation = models.TextField("Preparazione")
    image = models.ImageField(upload_to='images',null=True,blank=True)
    costo= models.CharField("Costo",max_length=10)
    time = models.IntegerField("Tempo di preparazione")
    week_recipe = models.BooleanField("Ricetta della settimana",default=False)
    spotlight_recipe = models.BooleanField("Ricetta in rilievo",default=False)

    class Meta:
        app_label = 'ricette'
        verbose_name_plural = "Ricette"
        ordering = ['nome']
    
    def __unicode__(self):
        return self.nome
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.nome)
        super(Ricetta, self).save()

    

    
    
