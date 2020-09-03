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
            'telefono_emergencia',
            'correo',
            'fecha_nacimiento',
            'descripcion',
            'sexo'
            ]
        lables = {
            'nombre' : 'Nombre:',
            'apellido' : 'Apellido:',
            'telefono': 'Telefono:',
            'telefono_emergencia' : 'Telefono de emergencia:',
            'correo' :'Correo electronico:',
            'fecha_nacimiento' : 'Fecha de Nacimiento',
            'descripcion': 'Descripcion:',
            'sexo': 'Sexo:'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_emergencia' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'})
        }