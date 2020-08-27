from django.db import models
#from anotacion.models import Anotacion

# Create your models here.
class Cita(models.Model):
    fecha = models.DateTimeField()
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado = models.CharField(max_length=10)
    comentario = models.CharField(max_length=50)
    paciente = models.IntegerField()