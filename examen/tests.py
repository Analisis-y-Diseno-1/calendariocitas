from django.test import TestCase
from cita.models import Cita
from .models import Examen
from users.models import Paciente
from datetime import datetime, timedelta, date
from django.urls import reverse, resolve

class ExaminationCreate(TestCase):
    def setUp(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        paciente=Paciente.objects.create(
            nombre = 'Henry',
            apellido = 'León',
            telefono = '12345678',
            telefono_emergencia = '12345679',
            correo = 'henrisco@gmail.com',
            fecha_nacimiento = '1995-12-12',
            direccion = 'zona 6',
            descripccion = 'Joven guapo :3',
            sexo = 'MASCULINO',
            )
        cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='Test', paciente=paciente).save()

        Examen(descripcion='Fractura en el pie', cita=cita, fecha=fecha).save()

    def test_examamination_model(self):
        examen = Examen.objects.all()[0]
        self.assertEquals(str(examen), "Fractura en el pie")