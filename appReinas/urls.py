from django.urls import path
from . import views

urlpatterns = [
    # Secciones dinámicas
    path('noticias', views.noticias, name='noticias'),
    path('jugadoras', views.jugadoras, name='jugadoras'),
    path('entrenadores', views.entrenadores, name='entrenadores'),
    path('directiva', views.directiva, name='directiva'),
    path('torneos', views.torneos, name='torneos'),
    path('eventos', views.eventos, name='eventos'),
    path('galeria', views.galeria, name='galeria'),
    path('enlaces', views.enlaces, name='enlaces'),
    path('historia', views.historia, name='historia'),
    path('contacto', views.contacto, name='contacto'),
    path('calendario', views.eventos, name='calendario'),
    path('tienda', views.tienda, name='tienda'),
    path('', views.index, name='index'),
]