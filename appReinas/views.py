from django.shortcuts import render
from .models import (
    Noticia, Jugadora, Entrenador, Directivo,
    Torneo, Evento, Galeria, Enlace, Historia
)

def index(request):
    noticias = Noticia.objects.order_by('-fecha')[:3]
    jugadoras = Jugadora.objects.all()[:3]
    torneos = Torneo.objects.order_by('-fecha')[:3]
    return render(request, 'index.html', {
        'noticias': noticias,
        'jugadoras': jugadoras,
        'torneos': torneos,
    })

def noticias(request):
    noticias = Noticia.objects.order_by('-fecha')
    return render(request, 'Noticias.html', {'noticias': noticias})

def jugadoras(request):
    jugadoras = Jugadora.objects.all()
    return render(request, 'Jugadoras.html', {'jugadoras': jugadoras})

def entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'Entrenadores.html', {'entrenadores': entrenadores})

def directiva(request):
    directivos = Directivo.objects.all()
    return render(request, 'Directiva.html', {'directivos': directivos})

def torneos(request):
    torneos = Torneo.objects.order_by('-fecha')
    return render(request, 'Torneos.html', {'torneos': torneos})

def eventos(request):
    eventos = Evento.objects.order_by('fecha')
    return render(request, 'Calendario.html', {'eventos': eventos})

def galeria(request):
    fotos = Galeria.objects.all()
    return render(request, 'Galeria.html', {'fotos': fotos})

def enlaces(request):
    enlaces = Enlace.objects.all()
    return render(request, 'Enlaces.html', {'enlaces': enlaces})

def historia(request):
    historia = Historia.objects.first()
    return render(request, 'Historia.html', {'historia': historia})

def contacto(request):
    return render(request, 'Contacto.html')

def tienda(request):
    return render(request, 'Tienda.html')
