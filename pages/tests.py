from django.test import TestCase, SimpleTestCase
from .views import HomePageView, AppointmentCreate
from django.urls import reverse, resolve

class HomepageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response,'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'fecha')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi! I should not be here')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AgendarCita(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('/agendar/cita/1')

    def test_agendar_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_agendar_url_name(self):
        response = self.client.get(reverse('crear_cita', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code,200)

    def test_agendar_template(self):
        self.assertTemplateUsed(self.response,'citas/crear_cita.html')
    
    def test_agendar_contains_correct_html(self):
        self.assertContains(self.response, 'planificada')
    
    def test_agendar_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi! I should not be here')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/agendar/cita/1')
        self.assertEqual(
            view.func.__name__,
            AppointmentCreate.as_view().__name__
        )