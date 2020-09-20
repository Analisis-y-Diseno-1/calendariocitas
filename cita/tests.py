from django.test import TestCase
from .models import Cita
from datetime import datetime, timedelta, date
from users.models import Paciente
from cita.models import Cita
# # Create your tests here.
# '''
# class ModelCitaTest(TestCase):

#     def test_create_city(self):
#         fecha = datetime.now()
#         hora = datetime.time()
#         Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=1001).save()

#         citas = Cita.objects.all()
#         self.assertEqual(citas[0].fecha, fecha)
#         self.assertEqual(citas[0].fecha_cita, fecha)
#         self.assertEqual(citas[0].hora_cita, hora)
#         self.assertEqual(citas[0].comentario, 'prueba')
#         self.assertEqual(citas[0].paciente, 1001)
#         self.assertEqual(citas[0].estado, 'Pendiente')
# '''

class ModelCitaTest(TestCase):

    def test_cancel_cita(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        paciente=Paciente.objects.create(
            nombre = 'Juan',
            apellido = 'Perez',
            telefono = '12345678',
            telefono_emergencia = '12345679',
            correo = 'juanperez@gmail.com',
            fecha_nacimiento = '2020-12-12',
            direccion = 'direccion de domicilio',
            descripccion = 'Persona de la tercera edad con problemas de respiracion',
            sexo = 'MASCULINO',
            )
        Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()

        citas = Cita.objects.all()
        self.assertEqual(citas[0].comentario, 'prueba')
        self.assertEqual(citas[0].paciente, paciente)
        self.assertEqual(citas[0].estado, 'Pendiente')
        self.assertNotEqual(citas[0].delete()[0],0 )#Es 0 si no elimino nada

class ModificarCita(TestCase):
    def test_modificar_cita(self):
        paciente = Paciente.objects.get(nombre='Lucia')
        test_cita = Cita.objects.create(fecha_cita='2020-09-25',hora_cita='06:30:00',estado='PENDIENTE',comentario='Editado1',paciente_id=paciente.id,fecha='2020-09-19 19:04:14.960231')

        getcita = Cita.objects.get(id=8)

        getcita.comentario = "Editado2"
        getcita.save()

        self.assertEqual(getcita.comentario,'Editado2')

        self.assertEqual(getcita.fecha_cita, '2020-09-25')
        self.assertEqual(getcita.hora_cita, '06:30:00')
        self.assertEqual(getcita.estado, 'PENDIENTE')
        self.assertEqual(getcita.comentario, 'Editado2')
        self.assertEqual(getcita.paciente_id, paciente.id)
        self.assertEqual(getcita.fecha, '2020-09-19 19:04:14.960231')

