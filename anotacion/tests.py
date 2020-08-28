from django.test import TestCase
from anotacion.models import Anotacion
from cita.models import Cita
from datetime import datetime

# Create your tests here.
<<<<<<< HEAD

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
=======
class AnnotationViewTest(TestCase):
    '''
    def setUp(self):
        #Create a meeting
        test_meeting = Cita.objects.create(fecha=datetime.now(), fecha_cita=datetime.now(), hora_cita=datetime.time(),
            estado='Pendiente', comentario='Hacre examen', paciente=1001)
        #test_meeting.save()

        #Create a annotation
        test_annotation = Anotacion.objects.create(id_cita=test_meeting.pk, descripcion='Tiene fiebre', fecha_hora=datetime.now())
        #test_annotation.save()
    '''

    def test_create_annotation(self):
        #esp = self.client.post(reverse('anotacion', kwargs={'pk':self.test_annotation.pk,}), {'renewal_date':valid_date_in_future} )
        #self.assertRedirects(resp, reverse('home') )
        #Create a meeting
        test_meeting = Cita.objects.create(fecha=datetime.now(), fecha_cita=datetime.now(), hora_cita=datetime.now(),
            estado='Pendiente', comentario='Hacre examen', paciente=1001)
        #Create a annotation
        fecha = datetime.now()
        test_annotation = Anotacion.objects.create(id_cita=test_meeting, descripcion='Tiene fiebre', fecha_hora=fecha)

        self.assertEqual(test_annotation.id_cita, test_meeting)
        self.assertEqual(test_annotation.descripcion, 'Tiene fiebre')
        self.assertEqual(test_annotation.fecha_hora, fecha)
        
>>>>>>> 2f6efda4a608e11d1fa6210d8a89eff68809c6c7
