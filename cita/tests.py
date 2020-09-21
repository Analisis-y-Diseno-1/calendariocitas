from django.test import TestCase
from .models import Cita, Receta
from datetime import datetime, timedelta, date



class test_url_receta_off(SimpleTestCase):

    def test_ingresar_pasajero(self):
        response = self.client.get('/ingresar_receta_off/')
        self.assertNotEqual(response.status_code, 404)

class test_isValidForm(TestCase):
    data={
            'fecha':'1996-02-17',
            'detalle_receta':'esto es una receta',
        }
    def test_valid_form(self):
        form = recetaOffForm(self.data)
        self.assertTrue(form.is_valid())

'''class EliminarRecetaTestCase(TestCase):
    def test_create_receta(self):
        now = datetime.now()
        #test_cista = Cita.objects.create(fecha=now, fecha_cita = now, estado = 'PENDIENTE',comentario ='Hello world')
        test_receta = Receta.objects.create(fecha=now, detalle_receta='Receta 222')
        #self.assertEqual(test_receta.detalle_receta,'Receta 222')   
        receta = Receta.objects.get(pk=test_receta.pk)
        self.assertEqual(receta.detalle_receta,'Receta')'''
        
        #pass
        #self.assertEqual(user.username, 'will')
        #self.assertEqual(user.email, 'will@email.com')
        #self.assertTrue(user.is_active)
        #self.assertFalse(user.is_staff)
        #self.assertFalse(user.is_superuser)
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