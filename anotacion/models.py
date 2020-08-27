from django.db import models
from datetime import datetime 
from ..cita.models import Cita

# Create your models here.
class Anotacion(models.Model):
    no_anotacion = models.AutoField(primary_key=True)
    id_cita = models.ForeignKey('Cita', db_column='id_cita', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    fecha_hora = models.DateTimeField(default=datetime.no

