from django.contrib import admin
from .models import (
    Noticia, Jugadora, Entrenador, Directivo,
    Torneo, Evento, Galeria, Enlace, Historia, Productos
)

# --- NOTICIA ---
class NoticiaAdmin(admin.ModelAdmin):
    # CORREGIDO: Usar 'fecha' en lugar de 'fecha_publicacion'
    # 'autor' eliminado, ya que no existe en el modelo Noticia
    list_display = ('titulo', 'fecha', 'imagen')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha',) 
    
admin.site.register(Noticia, NoticiaAdmin)

# --- JUGADORA ---
class JugadoraAdmin(admin.ModelAdmin):
    # CORREGIDO: Usar 'foto' en lugar de 'numero_camisa' (que no existe)
    list_display = ('nombre', 'posicion', 'foto')
    search_fields = ('nombre', 'posicion', 'foto','descripcion_breve', 'descripcion_completa')
    list_filter = ('posicion',)
admin.site.register(Jugadora, JugadoraAdmin)

# --- ENTRENADOR ---
class EntrenadorAdmin(admin.ModelAdmin):
    # CORREGIDO: Usar 'cargo' en lugar de 'rol'
    list_display = ('nombre', 'cargo', 'foto')
    search_fields = ('nombre', 'cargo', 'descripcion')
admin.site.register(Entrenador, EntrenadorAdmin)


# --- DIRECTIVO ---
class DirectivoAdmin(admin.ModelAdmin):
    # Correcto: 'nombre' y 'cargo' existen. Se añade 'foto'
    list_display = ('nombre', 'cargo', 'foto')
    search_fields = ('nombre', 'cargo', 'descripcion')
admin.site.register(Directivo, DirectivoAdmin)


# --- TORNEO ---
class TorneoAdmin(admin.ModelAdmin): # Cambiado 'torneoAdmin' a 'TorneoAdmin' (Convención)
    # CORREGIDO: Usar 'titulo' y 'fecha' en lugar de 'nombre', 'fecha_inicio', 'fecha_fin'
    list_display = ('titulo', 'fecha', 'imagen')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha',)
admin.site.register(Torneo, TorneoAdmin)


# --- EVENTO ---
class EventoAdmin(admin.ModelAdmin):
    # CORREGIDO: Usar 'fecha' y 'lugar' en lugar de 'fecha_evento', 'ubicacion'
    list_display = ('titulo', 'fecha', 'lugar')
    search_fields = ('titulo', 'descripcion', 'lugar')
    list_filter = ('fecha',)
admin.site.register(Evento, EventoAdmin)


# --- GALERIA ---
class GaleriaAdmin(admin.ModelAdmin):
    # CORREGIDO: Usar 'imagen' y 'descripcion'. Eliminado 'fecha_subida' (que no existe)
    list_display = ('titulo', 'descripcion', 'imagen')
    search_fields = ('titulo', 'descripcion')
    # list_filter = ('fecha_subida',)  # Eliminado por no existir el campo
admin.site.register(Galeria, GaleriaAdmin)

# --- ENLACE ---
class EnlaceAdmin(admin.ModelAdmin):
    # CORREGIDO: Usar 'titulo' en lugar de 'nombre'
    list_display = ('titulo', 'url')
    search_fields = ('titulo', 'url')

admin.site.register(Enlace, EnlaceAdmin)

# --- HISTORIA ---
class HistoriaAdmin(admin.ModelAdmin):
    # CORREGIDO: El modelo Historia solo tiene 'contenido'. Se puede usar __str__
    # Se añade un campo personalizado para mostrar las primeras 50 letras del contenido
    list_display = ('id', '__str__', 'vista_previa')
    search_fields = ('contenido',)
    
    # Método auxiliar para mostrar una vista previa del contenido en la lista
    def vista_previa(self, obj):
        return obj.contenido[:50] + '...' if len(obj.contenido) > 50 else obj.contenido
    vista_previa.short_description = 'Contenido'

# NOTA: Historia solo tiene 'contenido', 'titulo' y 'fecha_creacion' fueron eliminados
# en la definición de tu modelo, por lo que se ajustó el list_display.

admin.site.register(Historia, HistoriaAdmin)

class adminProductos(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'imagen','descripcion')
    search_fields = ('nombre', 'descripcion')

admin.site.register(Productos, adminProductos)