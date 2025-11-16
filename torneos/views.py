from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Torneo

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
