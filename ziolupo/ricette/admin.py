from django.contrib import admin
from ziolupo.ricette.models import Portata,Categoria,Ricetta


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    
class RicetteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Portata)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Ricetta,RicetteAdmin)

