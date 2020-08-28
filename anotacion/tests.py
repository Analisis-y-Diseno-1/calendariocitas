from django.test import TestCase

# Create your tests here.

from anotacion.models import Anotacion
from django.urls import reverse

class ListaAnotacionesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create 13 anotaciones for tests
        number_of_anotaciones = 13
        for anotacion_num in range(number_of_anotaciones):
            Anotacion.objects.create(descripcion='Ejemplo anotacion %s' % author_num)
            
    def test_view_url_exists_at_desired_location(self): 
        #Verifica que la url exista
        resp = self.client.get('/listado_anotaciones') 
        self.assertEqual(resp.status_code, 200) 