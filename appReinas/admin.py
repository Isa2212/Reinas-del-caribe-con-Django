from django.contrib import admin
from .models import (
    Noticia, Jugadora, Entrenador, Directivo,
    Torneo, Evento, Galeria, Enlace, Historia, Productos, ActividadCalendario
)

# --- NOTICIA ---
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'imagen')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha',)

admin.site.register(Noticia, NoticiaAdmin)

# --- JUGADORA ---
class JugadoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'foto')
    search_fields = ('nombre', 'posicion', 'descripcion_breve', 'descripcion_completa')
    list_filter = ('posicion',)

admin.site.register(Jugadora, JugadoraAdmin)

# --- ENTRENADOR ---
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'foto')
    search_fields = ('nombre', 'cargo', 'descripcion')

admin.site.register(Entrenador, EntrenadorAdmin)

# --- DIRECTIVO ---
class DirectivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'foto')
    search_fields = ('nombre', 'cargo', 'descripcion')

admin.site.register(Directivo, DirectivoAdmin)

# --- TORNEO ---
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'imagen')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha',)

admin.site.register(Torneo, TorneoAdmin)

# --- EVENTO ---
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'lugar')
    search_fields = ('titulo', 'descripcion', 'lugar')
    list_filter = ('fecha',)

admin.site.register(Evento, EventoAdmin)

# --- GALERIA ---
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'imagen')
    search_fields = ('titulo', 'descripcion')

admin.site.register(Galeria, GaleriaAdmin)

# --- ENLACE ---
class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url')
    search_fields = ('titulo', 'url')

admin.site.register(Enlace, EnlaceAdmin)

# --- HISTORIA ---
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'vista_previa')
    search_fields = ('contenido',)

    def vista_previa(self, obj):
        return obj.contenido[:50] + '...' if len(obj.contenido) > 50 else obj.contenido

    vista_previa.short_description = 'Contenido'

admin.site.register(Historia, HistoriaAdmin)

# --- PRODUCTOS ---
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'imagen', 'descripcion')
    search_fields = ('nombre', 'descripcion')

admin.site.register(Productos, ProductosAdmin)

# --- Calenario ---
class ActividadCalendarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha',)

admin.site.register(ActividadCalendario, ActividadCalendarioAdmin)
 