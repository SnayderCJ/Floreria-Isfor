from django.contrib import admin
from .models import Categoria, ArregloFloral
from django.utils.html import format_html

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(ArregloFloral)
class ArregloFloralAdmin(admin.ModelAdmin):
    list_display = ['mostrar_imagen', 'nombre', 'precio_base', 'disponible', 'categoria']
    list_filter = ['disponible', 'categoria']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio_base', 'disponible']

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px;" />', obj.imagen.url)
        return "Sin imagen"
    
    mostrar_imagen.short_description = 'Imagen'