from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from anotacion.forms import AnotacionForm
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
    
    def get_form(self):
        form = self.form_class(instance=AnotacionForm) # instantiate the form

        # modify the form fields
        # form.fields['primary_purpose_business_use'].label = "Primary purpose/business use"
        # form.fields['secondary_purpose_business_uses'].label = "Secondary purpose/business uses"

        return form
    
    def get_context_data(self, **kwargs):
        context = super(AppointmentDetailView, self).get_context_data(**kwargs)
        context.update({
            'anotacion_form': AnotacionForm # get the form instance
        })

        return context

class AppointmentCreate(TemplateView):
    template_name = 'citas/crear_cita.html'