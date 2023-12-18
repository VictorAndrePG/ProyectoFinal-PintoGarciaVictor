from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    puntaje = models.IntegerField(default=0)
    fecha_ultimo_cambio = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='equipos/', blank=True, null=True)
    def __str__(self):
        return f"Equipo: {self.nombre} - Puntaje {self.puntaje} "


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return f"Mostrando jugador: {self.nombre} {self.apellido} "


class Entrenador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    puntaje = models.IntegerField(default=0)
    def __str__(self):
        return f"Mostrando entrenador: {self.nombre} {self.apellido} "