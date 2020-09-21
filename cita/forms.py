from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Receta
from django import forms
from datetime import datetime


class recetaOffForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'detalle_receta'
            ]
        labels = {
            'detalle_receta': 'Descripcion:'
        }
        widgets = {
            'detalle_receta': forms.Textarea(attrs={'class':'form-control'})
        }