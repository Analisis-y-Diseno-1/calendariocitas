from django.urls import path
from .views import HomePageView
from anotacion.views import crear_anotacion

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('anotacion/', crear_anotacion, name='anotacion'),
]