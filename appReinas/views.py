from django.shortcuts import render
import calendar
from .models import (
    Noticia, Jugadora, Entrenador, Directivo,
    Torneo, Evento, Galeria, Enlace, Historia,Productos, ActividadCalendario
)

def index(request):
    noticias = Noticia.objects.order_by('-fecha')[:5]
    jugadoras = Jugadora.objects.all()[:3]
    productos = Productos.objects.all()[:4]
    torneos = Torneo.objects.order_by('-fecha')[:3]
    return render(request, 'index.html', {
        'noticias': noticias,
        'jugadoras': jugadoras,
        'productos': productos,
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
    productos = Productos.objects.all()
    return render(request, 'Tienda.html', {'productos': productos})

def generar_mes(anio, mes):
    cal = calendar.Calendar()
    semanas = cal.monthdayscalendar(anio, mes)

    # CARGAR ACTIVIDADES DEL MES DESDE admin
    eventos_mes = ActividadCalendario.objects.filter(
        fecha__year=anio,
        fecha__month=mes
    )

    # MAPEAR EVENTOS POR DÍA
    eventos_por_dia = {}
    for e in eventos_mes:
        eventos_por_dia[e.fecha.day] = e

    # CREAR ESTRUCTURA PARA LA PLANTILLA
    semanas_vista = []
    for semana in semanas:
        fila = []
        for d in semana:
            if d == 0:
                fila.append({"numero": 0, "evento": None})
            else:
                fila.append({
                    "numero": d,
                    "evento": eventos_por_dia.get(d)
                })
        semanas_vista.append(fila)

    return {
        "nombre": calendar.month_name[mes],
        "semanas": semanas_vista
    }

def calendario(request):
    anio = 2025  # Puedes luego hacerlo dinámico

    meses = [
        generar_mes(anio, 3),
        generar_mes(anio, 4),
        generar_mes(anio, 5),
    ]

    return render(request, "Calendario.html", {"meses": meses})
