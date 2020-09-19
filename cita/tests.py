from django.test import TestCase, SimpleTestCase
from .models import Cita, Receta
from datetime import datetime, timedelta, date
from users.models import Paciente
from django.urls import reverse, resolve
from .views import Cita
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

class RecetaCreate(TestCase):
    
    def setUp(self):
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
        cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()

        Receta(detalle_receta='Tiene dolor de garganta', cita=cita, fecha=fecha).save()
        #receta = Receta.objects.create(detalle_receta='Tiene dolor de garganta',)
        self.response = self.client.get('/crear_receta/6')

    def test_agendar_status_code(self):
        self.assertEqual(self.response.status_code,302)

    def test_crear_recete_url(self):
        response = self.client.get(reverse('crear_receta', kwargs={'id': '6'}))
        self.assertEqual(response.status_code,302)

    def test_crear_recetas_url_resolves_create_recetasview(self):
        view = resolve('/crear_receta/6')
        self.assertEqual(
            view.func.__name__,
            RecetaCreate.__name__
        )
    
    def test_crear_receta(self):
        receta = Receta.objects.all()[0]
        self.assertEqual(receta.detalle_receta, 'Tiene dolor de garganta')