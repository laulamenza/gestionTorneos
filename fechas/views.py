from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fecha, Participacion
from torneos.models import Torneo


# Crear Fecha
def crear_fecha(request, torneo_id):
    torneo = get_object_or_404(Torneo, pk=torneo_id)
    if request.method == 'POST':
        numero = torneo.fechas.count() + 1
        fecha = request.POST.get('fecha')
        club_organizador = request.POST.get('club_organizador')

        Fecha.objects.create(
            torneo=torneo,
            numero=numero,
            fecha=fecha,
            club_organizador=club_organizador
        )
        return redirect('torneos:detalle', pk=torneo.pk)

    # Si querés mostrar formulario aparte
    numero_sugerido = torneo.fechas.count() + 1
    return render(request, 'fechas/crear_fecha.html', {
        'torneo': torneo,
        'numero_sugerido': numero_sugerido,
        'clubes': Fecha.CLUBES,
    })


# Editar Fecha
def editar_fecha(request, pk):
    fecha = get_object_or_404(Fecha, pk=pk)
    if request.method == 'POST':
        fecha.fecha = request.POST.get('fecha')
        fecha.club_organizador = request.POST.get('club_organizador')
        fecha.save()
        return redirect('torneos:detalle', pk=fecha.torneo.pk)

    return render(request, 'fechas/editar_fecha.html', {
        'fecha': fecha,
        'clubes': Fecha.CLUBES,
    })


# Eliminar Fecha
def eliminar_fecha(request, pk):
    fecha = get_object_or_404(Fecha, pk=pk)
    torneo_id = fecha.torneo.pk
    if request.method == 'POST':
        fecha.delete()
        return redirect('torneos:detalle', pk=torneo_id)

    return render(request, 'fechas/eliminar_fecha.html', {'fecha': fecha})


# Listar Fechas de un Torneo
def listar_fechas(request, torneo_id):
    torneo = get_object_or_404(Torneo, pk=torneo_id)
    fechas = torneo.fechas.all().order_by('numero')
    return render(request, 'fechas/listar_fechas.html', {
        'torneo': torneo,
        'fechas': fechas,
    })

from jugadores.models import Jugador

def detalle_fecha(request, pk):
    fecha = get_object_or_404(Fecha, pk=pk)
    participaciones = fecha.participaciones.all().order_by('-puntaje')

    if request.method == 'POST':
        jugador_id = request.POST.get('jugador')
        puntaje = int(request.POST.get('puntaje'))

        jugador = get_object_or_404(Jugador, pk=jugador_id)
        nueva_participacion = Participacion.objects.create(
            fecha=fecha,
            jugador=jugador,
            puntaje=puntaje,
            posicion=0  # temporal
        )

        # recalcular posiciones según puntaje
        participaciones_actualizadas = fecha.participaciones.all().order_by('-puntaje')
        for idx, p in enumerate(participaciones_actualizadas, start=1):
            p.posicion = idx
            p.save()

        return redirect('fechas:detalle', pk=fecha.pk)

    jugadores = Jugador.objects.all()
    return render(request, 'fechas/detalle_fecha.html', {
        'fecha': fecha,
        'participaciones': participaciones,
        'jugadores': jugadores,
    })

 
