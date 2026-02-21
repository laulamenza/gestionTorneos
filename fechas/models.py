from django.db import models
from torneos.models import Torneo
from jugadores.models import Jugador

class Fecha(models.Model):
    CLUBES = [
        ('NEWBERY', 'Newbery'),
        ('CAI', 'Cai'),
        ('HURACAN', 'Huracán'),
        ('SAN_MANUEL', 'San Manuel'),
    ]

    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='fechas')
    club_organizador = models.CharField(max_length=100, choices=CLUBES, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f"Fecha {self.numero} - {self.torneo.nombre} ({self.fecha})"


class Participacion(models.Model):
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE, related_name='participaciones')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='participaciones')
    posicion = models.PositiveIntegerField()
    puntaje = models.PositiveIntegerField()

    class Meta:
        unique_together = ('fecha', 'jugador')

    def __str__(self):
        return f"{self.jugador} en {self.fecha} - Pos {self.posicion}, Pts {self.puntaje}"
