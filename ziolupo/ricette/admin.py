from django.contrib import admin
from ziolupo.ricette.models import Categoria,Ricetta


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    
class RicetteAdmin(admin.ModelAdmin):

    list_display= ('nome','categoria', 'image_img',)
    readonly_fields = ('image_img',)

    fieldsets = (
        (None, {
            'fields': ('nome', 'categoria', 'image', 'image_img', )
        }),
        ('Caratteristiche', {
            'classes': ('collapse',),
            'fields': ('costo', 'time', 'difficulty')
        }),
        ('Ingredienti', {
            'classes': ('collapse',),
            'fields': ('ingredients', )
        }),
        ('Preparazione', {
            'classes': ('collapse',),
            'fields': ('preparation', )
        }),
    )

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Ricetta,RicetteAdmin)

