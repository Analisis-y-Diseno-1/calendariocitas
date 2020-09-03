from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(blank=True, null=True)
    telefono_emergencia = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField() #DateField(input_formats=settings.DATE_INPUT_FORMATS, null=True, blan=True) para introducir la fecha dd-mm-DDDD
    direccion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    sexo = models.CharField(max_length=15)