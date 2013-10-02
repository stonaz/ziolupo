from django.contrib import admin
from ziolupo.ricette.models import Categoria,Ricetta


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    
class RicetteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Ricetta,RicetteAdmin)

