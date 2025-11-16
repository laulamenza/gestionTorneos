from django.db import models
from jugadores.models import Jugador  # Ajustá el import según tu estructura

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_fechas = models.IntegerField(help_text="Cantidad total de fechas que tiene el torneo")

    def __str__(self):
        return self.nombre
    
    #def fechas_jugadas(self):
    #return self.fechas.count()


class PuntajeTorneo(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='puntajes')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='puntajes_torneos')
    puntaje_total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.jugador} - {self.torneo}: {self.puntaje_total}"

