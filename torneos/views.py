from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Torneo
from django.shortcuts import render, get_object_or_404
from fechas.models import Fecha, Participacion
from django.db.models import Sum, Count

class TorneoListView(ListView):
    model = Torneo
    template_name = 'torneos/torneo_list.html'
    context_object_name = 'torneos'


class TorneoCreateView(CreateView):
    model = Torneo
    fields = ['nombre', 'cantidad_fechas']
    template_name = 'torneos/torneo_form.html'
    success_url = reverse_lazy('torneos:lista')


class TorneoUpdateView(UpdateView):
    model = Torneo
    fields = ['nombre', 'cantidad_fechas']
    template_name = 'torneos/torneo_form.html'
    success_url = reverse_lazy('torneos:lista')


class TorneoDeleteView(DeleteView):
    model = Torneo
    
    success_url = reverse_lazy('torneos:lista')
    


def detalle_torneo(request, pk):
    torneo = get_object_or_404(Torneo, pk=pk)

    fechas = torneo.fechas.all().order_by('numero')
    fechas_jugadas = fechas.count()

    posiciones = (
        Participacion.objects
        .filter(fecha__torneo=torneo)
        .values('jugador__nombre', 'jugador__apellido', 'jugador__categoria')
        .annotate(total_puntos=Sum('puntaje'), 
                  total_fechas=Count('fecha', distinct=True), 
                  )
        .order_by('-total_puntos')
    )

    proxima_fecha = fechas_jugadas + 1

    context = {
        'torneo': torneo,
        'fechas': fechas,
        'fechas_jugadas': fechas_jugadas,
        'posiciones': posiciones,
        'proxima_fecha': proxima_fecha,
        'clubes': Fecha.CLUBES,
    }
    return render(request, 'torneos/detalle_torneo.html', context)


