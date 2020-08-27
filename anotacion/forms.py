from django import forms
from anotacion.models import Anotacion

#from anotacion.models import models
class AnotacionForm(forms.ModelForm):
    class Meta:
        model = Anotacion
        fields = [
            'descripcion',
        ]
        labels = {
            'descripcion': 'Descripción',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form_control', 'cols': 15, 'rows': 3}),
        }

