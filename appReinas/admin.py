from django.contrib import admin
from .models import (
    Noticia, Jugadora, Entrenador, Directivo,
    Torneo, Evento, Galeria, Enlace, Historia
)

admin.site.register(Noticia)
    # list_display()
admin.site.register(Jugadora)
admin.site.register(Entrenador)
admin.site.register(Directivo)
admin.site.register(Torneo)
admin.site.register(Evento)
admin.site.register(Galeria)
admin.site.register(Enlace)
admin.site.register(Historia)
