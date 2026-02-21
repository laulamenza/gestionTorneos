from django.urls import path
from .views import *

app_name = 'fechas'

urlpatterns = [
    path('crear/<int:torneo_id>/', crear_fecha, name='crear'), 
    path('editar/<int:pk>/', editar_fecha, name='editar'), 
    path('eliminar/<int:pk>/', eliminar_fecha, name='eliminar'), 
    path('listar/<int:torneo_id>/', listar_fechas, name='listar'),
    path('<int:pk>/', detalle_fecha, name='detalle'),
]
