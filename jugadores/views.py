from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .models import Jugador
from django.shortcuts import redirect
from django.http import JsonResponse


class JugadorListView(ListView):
    model = Jugador
    template_name = 'jugadores/jugadores.html'  # Ubicación y nombre del template
    context_object_name = 'jugadores'  # Nombre que se usará en el template para acceder a la lista
    
class JugadorDeleteView(DeleteView):
    model = Jugador  
    success_url = reverse_lazy('jugadores:lista')  # Redirige a la lista de jugadores tras eliminar uno

def crear_jugador(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        categoria = request.POST.get('categoria')
        handicap = request.POST.get('handicap')
        
        # Crear el jugador en la base de datos
        jugador = Jugador.objects.create(
            nombre=nombre,
            apellido=apellido,
            categoria=categoria,
            handicap=handicap
        )
        
        # Respuesta JSON para el modal (opcional)
        return redirect('jugadores:lista')
    
    # Si no es POST, redirigir a la lista de jugadores
    return redirect('jugadores:lista')

def editar_jugador(request, pk):
    jugador = Jugador.objects.get(pk=pk)
    if request.method == 'POST':
        jugador.nombre = request.POST.get('nombre')
        jugador.apellido = request.POST.get('apellido')
        jugador.categoria = request.POST.get('categoria')
        jugador.handicap = request.POST.get('handicap')
        jugador.save()
        return redirect('jugadores:lista')

from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from fechas.models import Participacion
from .models import Jugador

def detalle_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)

    participaciones = Participacion.objects.filter(jugador=jugador)

    # estadísticas
    total_fechas = participaciones.values('fecha').distinct().count()
    fechas_ganadas = participaciones.filter(posicion=1).count()
    total_puntos = participaciones.aggregate(Sum('puntaje'))['puntaje__sum'] or 0
    promedio_puntos = total_puntos / total_fechas if total_fechas > 0 else 0

    context = {
        'jugador': jugador,
        'total_fechas': total_fechas,
        'fechas_ganadas': fechas_ganadas,
        'total_puntos': total_puntos,
        'promedio_puntos': promedio_puntos,
        'participaciones': participaciones.order_by('fecha__numero'),
    }
    return render(request, 'jugadores/detalle_jugador.html', context)

