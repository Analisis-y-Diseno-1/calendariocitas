from django import forms
from django.forms import ModelForm
from users.models import Paciente

#from anotacion.models import models
class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'telefono_emergencia'
            ]

class RawProductForm(forms.Form):
    nombre      = forms.CharField()
    apellido    = forms.CharField()
    telefono    = forms.CharField()