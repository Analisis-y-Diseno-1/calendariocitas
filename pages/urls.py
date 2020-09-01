from django.urls import path
from anotacion.views import crear_anotacion,modificar_anotacion,listado_anotaciones, eliminar_anotacion
from users.views import listado_pacientes,modificar_paciente
from .views import HomePageView, AppointmentsListView, AppointmentDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('citas', AppointmentsListView.as_view(), name='citas'),
    path('citas/<int:pk>', AppointmentsListView.as_view(), name='cita_detail'),
    path('anotacion/', crear_anotacion, name='anotacion'),
    path('listado_anotaciones/', listado_anotaciones, name='listado_anotaciones'),
    path('modificar_anotacion/<id>', modificar_anotacion, name='modificar_anotacion'),
    path('eliminar_anotacion/<id>', eliminar_anotacion, name='eliminar_anotacion'),
    path('listado_pacientes/', listado_pacientes, name='listado_pacientes'),
    path('modificar_paciente/<correo>', modificar_paciente, name='modificar_paciente'),
]