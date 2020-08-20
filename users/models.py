from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

class CustomUser(AbstractUser):
    pass


# PK -- ID
# NOmbre paciente
# telefono
# correo
# fecha de nacimiento
# sexo
# direccion
# Observacion(alergias o algo asi)
class Paciente(models.Model):  

    MASCULINO = "M"
    FEMENINO = "F"
    
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    nombre = models.CharField(max_length=250, blank=False, null=False)
    telefono = PhoneField(blank=True, help_text="Numero telefonico de contacto")
    correo = models.EmailField(max_length=254, blank=False, null=False)
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    fecha_de_registro = models.DateTimeField(auto_now=False, auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True, auto_now_add=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default=MASCULINO)
    direccion = models.CharField(max_length=250)
    observacion = models.CharField(max_length=250)


    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Paciente_detail", kwargs={"pk": self.pk})
