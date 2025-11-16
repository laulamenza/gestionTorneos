from django.urls import path
from .views import *

app_name = 'torneos'

urlpatterns = [
    path('lista/', TorneoListView.as_view(), name='lista'),
    path('crear/', TorneoCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', TorneoUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', TorneoDeleteView.as_view(), name='eliminar'),
]
