from django.contrib import admin
from .models import (
    Noticia, Jugadora, Entrenador, Directivo,
    Torneo, Evento, Galeria, Enlace, Historia
)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'autor')
    search_fields = ('titulo', 'contenido', 'autor__username')
    list_filter = ('fecha_publicacion',)
admin.site.register(Noticia, NoticiaAdmin)
    # list_display()
class JugadoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'numero_camisa')
    search_fields = ('nombre', 'posicion')
    list_filter = ('posicion',)
admin.site.register(Jugadora, JugadoraAdmin)

class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol')
    search_fields = ('nombre', 'rol')
admin.site.register(Entrenador, EntrenadorAdmin)


class DirectivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo')
    search_fields = ('nombre', 'cargo')
admin.site.register(Directivo, DirectivoAdmin)


class torneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre',)
    list_filter = ('fecha_inicio',)
admin.site.register(Torneo, torneoAdmin)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_evento', 'ubicacion')
    search_fields = ('titulo', 'descripcion', 'ubicacion')
    list_filter = ('fecha_evento',)
admin.site.register(Evento, EventoAdmin)


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')
    search_fields = ('titulo',)
    list_filter = ('fecha_subida',)
admin.site.register(Galeria, GaleriaAdmin)

class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url')
    search_fields = ('nombre',)

admin.site.register(Enlace, EnlaceAdmin)

class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
admin.site.register(Historia, HistoriaAdmin)