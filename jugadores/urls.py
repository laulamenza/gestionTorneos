from django.urls import path
from .views import *

app_name = 'jugadores'

urlpatterns = [
    path('lista/', JugadorListView.as_view(), name='lista'),
    path('crear/', crear_jugador, name='crear-jugador'),
    path('eliminar/<int:pk>/', JugadorDeleteView.as_view(), name='jugador-eliminar'),
    path('editar/<int:pk>/', editar_jugador, name='jugador-editar'),
    path('<int:pk>/', detalle_jugador, name='detalle'),
]
