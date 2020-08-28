
from django import forms
from django.forms import ModelForm
from anotacion.models import Anotacion

class CardAnotacion_form(ModelForm):
    
    class Meta:
        model = Anotacion
        fields = ['descripcion']