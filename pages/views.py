from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from cita.models import Cita

class HomePageView(TemplateView):
    template_name = 'home.html'

class AppointmentsListView(ListView):
    model = Cita
    context_object_name = 'cita_list'
    template_name = 'citas/lista_citas.html'


class AppointmentDetailView(DetailView):
    model = Cita
    context_object_name = 'cita'
    template_name = 'citas/cita_detail.html'