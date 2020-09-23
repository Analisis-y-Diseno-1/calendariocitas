from django.shortcuts import render
from cita.models import Cita
from .models import Examen
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from cita.forms import recetaOffForm
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Create your views here.
#def ExaminationCreate(request, pk):

#    return HttpResponseRedirect('/citas/'+pk)

class ExaminationCreate(DetailView):
    model = Cita
    context_object_name = 'cita'
    template_name = 'examen/examination_create_form.html'
    
