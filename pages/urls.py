from django.urls import path
from .views import HomePageView
from anotacion.views import crear_anotacion,modificar_anotacion,listado_anotaciones, eliminar_anotacion

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('anotacion/', crear_anotacion, name='anotacion'),
    path('listado_anotaciones/', listado_anotaciones, name='listado_anotaciones'),
    path('modificar_anotacion/<id>', modificar_anotacion, name='modificar_anotacion'),
    path('eliminar_anotacion/<id>', eliminar_anotacion, name='eliminar_anotacion'),
]