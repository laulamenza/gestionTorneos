from django.db import models

class Jugador(models.Model):
    CATEGORIA_CHOICES = [
        ('1ra', 'Primera'),
        ('2da', 'Segunda'),
        ('3ra', 'Tercera'),
        ('3raB', 'Tercera B'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=10,
        choices=CATEGORIA_CHOICES,
        default='3ra',  # Valor por defecto (opcional)
    )
    handicap = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.categoria}"
