from django.db import models
from datetime import datetime 

# Create your models here.
class Anotacion(models.Model):
    no_anotacion = models.AutoField(primary_key=True)
    id_cita = models.IntegerField(blank=True, null=True) #Cambiar esto porque hay que esperar la tabla cita
    descripcion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField(default=datetime.now)

