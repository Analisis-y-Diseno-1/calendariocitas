from django.db import models
from anotacion.models import Anotacion

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10)
    comentario = models.CharField(max_length=50)
    anotacion = models.ForeignKey(Anotacion, on_delete=models.CASCADE)