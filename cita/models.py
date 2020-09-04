from django.db import models
from django.urls import reverse
# Create your models here.
class Cita(models.Model):
    ESTADO_OPCIONES = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDA', 'Atendida'),
        ('Cancelada', 'Cancelada'),
    ]
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='PENDIENTE')
    comentario = models.CharField(max_length=50)
    # paciente = models.IntegerField()
    paciente = models.ForeignKey("users.Paciente", related_name="citas", on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("cita_detail", kwargs={"pk": self.pk})
    