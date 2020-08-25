from django.db import models
from datetime import datetime 

# Create your models here.
class Anotacion(models.Model):
    no_anotacion = models.AutoField(primary_key=true)
    id_cita = models.IntegerField(blank=true, null=true) #Cambiar esto porque hay que esperar la tabla cita
    descripcion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField(default=datetime.now)

