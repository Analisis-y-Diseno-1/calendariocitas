from django.db import models
from django.urls import reverse
# Create your models here.
class Cita(models.Model):
    fecha = models.DateTimeField()
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado = models.CharField(max_length=10)
    comentario = models.CharField(max_length=50)
    paciente = models.IntegerField()

    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("cita_detail", kwargs={"pk": self.pk})
    