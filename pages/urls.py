from django.urls import path
from anotacion.views import crear_anotacion,modificar_anotacion,listado_anotaciones, eliminar_anotacion, annotationCreate
from users.views import listado_pacientes,modificar_paciente, ingresar_paciente, detalle_paciente,reporte_historial_clinico
from cita.views import appointment_create, appointment_update,appointment_delete,appointment_serve, RecetaCreate,ingresar_receta_off,eliminar_receta, modificar_receta
from .views import HomePageView, AppointmentsListView, AppointmentDetailView
from .views import AppointmentCreate
from .views import SearchResultsListView
from .views import RecetasListView, RecetasDetailView
from .views import modificar_cita
from examen.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # Busquedas
    path('search_results/', SearchResultsListView.as_view(), name="search_by_name"),
    # Recetas
    path('recetas/', RecetasListView.as_view(), name="recetas"),
    path('recetas/<int:pk>', RecetasDetailView.as_view(), name="receta_detail"),
    path('crear_receta/<id>', RecetaCreate, name='crear_receta'),
    path('ingresar_receta_off/', ingresar_receta_off, name='anotacion'),
    path('eliminar_receta/<id>', eliminar_receta, name='eliminar_receta'),
    path('modificar_receta/<id>', modificar_receta, name='modificar_receta'),
    
    #  E X A M E N
    path('crear_examen/<pk>', ExaminationCreate.as_view(), name='crear_examen'),
    path('accion_crear/<pk>', ExaminationActionCreate, name='accion_crear'),
    path('listado_examenes/', ExaminationListView, name='ExaminationListView'),
    path('modificar_examen/<pk>/', ExaminationEdit, name='modificar_examen'),
    path('eliminar_examen/<pk>/', ExaminationDelete, name='eliminar_examen'),
    
    # CITAS
    path('citas', AppointmentsListView.as_view(), name='citas'),
    path('citas/<int:pk>', AppointmentDetailView.as_view(), name='cita_detail'),
    path('agendar/cita/<int:pk>/<str:name>', AppointmentCreate.as_view(), name='crear_cita'),
    path('act_crear_cita/<int:pk>', appointment_create, name="appointment_create"),
    path('eliminar_cita/<int:pk>', appointment_delete, name="eliminar_cita"),
    path('atender_cita/<int:pk>', appointment_serve, name="atender_cita"),
    path('modificar_cita/<int:pk>/', modificar_cita, name="modificar_cita"),
    # ANOTACIONES
    path('anotacion/', crear_anotacion, name='anotacion'),
    path('crear_anotacion/<id>', annotationCreate, name='crear_anotacion'),
    path('listado_anotaciones/', listado_anotaciones, name='listado_anotaciones'),
    path('modificar_anotacion/<id>', modificar_anotacion, name='modificar_anotacion'),
    path('eliminar_anotacion/<id>', eliminar_anotacion, name='eliminar_anotacion'),
    # PACIENTES
    path('listado_pacientes/', listado_pacientes, name='listado_pacientes'),
    path('modificar_paciente/<correo>', modificar_paciente, name='modificar_paciente'),
    path('ingresar_paciente/', ingresar_paciente, name='ingresar_paciente'),
    path('detalle_paciente/<correo>', detalle_paciente, name='detalle_paciente'),
    # REPORTES historial clinico
    path('historial_clinico/', reporte_historial_clinico.as_view(), name='reporte_historial_clinico'),  
    #path('historial_clinico/<int:pk>', reporte_historial_clinico, name='reporte_historial_clinico'),
]