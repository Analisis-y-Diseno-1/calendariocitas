from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .models import Paciente
import datetime


class PacienteTests(TestCase):


    def setUp(self):
        Paciente.objects.create(
            nombre="Brandon Chitay",
            telefono="+50247529761",
            correo="antonchitay@gmail.com",
            sexo="M",
            direccion="Planeta Tierra",
            observacion="Vivo en la tierra",
            fecha_de_nacimiento="1996-11-07"
        )

    def test_create_paciente(self):
        paciente = Paciente.objects.create(
            nombre="Brandon Chitay",
            telefono="+50247529761",
            correo="antonchitay@gmail.com",
            sexo="M",
            direccion="Planeta Tierra",
            observacion="Vivo en la tierra",
            fecha_de_nacimiento="1996-11-07"
        )

        self.assertEqual(paciente.telefono, "+50247529761")
        self.assertEqual(paciente.correo,"antonchitay@gmail.com")
        self.assertEqual(paciente.sexo, "M")
        self.assertEqual(paciente.direccion, "Planeta Tierra")
        self.assertEqual(paciente.observacion, "Vivo en la tierra")
        self.assertEqual(paciente.fecha_de_nacimiento, '1996-11-07')
        
    def test_paciente_exist(self):
        paciente = Paciente.objects.filter(nombre="Brandon Chitay")
        self.assertEqual(len(paciente), 1)

    def test_paciente_does_not_exist(self):
        paciente = Paciente.objects.filter(nombre="Brandon Anthony")
        self.assertEqual(len(paciente), 0)
    
    def test_paciente_modified(self):
        Paciente.objects.filter(nombre="Brandon Chitay").update(nombre="Anthony Chitay")
        paciente = Paciente.objects.get(nombre="Anthony Chitay")
        self.assertEqual(paciente.telefono, "+50247529761")


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase): # new

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)