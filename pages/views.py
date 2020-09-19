from django.shortcuts import render
from users.models import Paciente
from django.views.generic import TemplateView, ListView, DetailView
from anotacion.forms import AnotacionForm
from cita.forms import RecetaForm
from cita.models import Cita, Receta
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

class AppointmentsListView(ListView):
    model = Cita
    context_object_name = 'cita_list'
    template_name = 'citas/lista_citas.html'
    def get_queryset(self):
        filter_val = self.request.GET.get('q', 'give-default-value')
        print(filter_val)
        try:
            new_context = Cita.objects.filter(
                fecha_cita=filter_val,
            )
            return new_context
        except:
            new_context = Cita.objects.all()
            return new_context

        

class RecetasListView(ListView):
    model = Receta
    context_object_name="recetas"
    template_name='recetas/lista_de_recetas.html'

class RecetasDetailView(DetailView):
    model = Receta
    context_object_name="receta"
    template_name='recetas/detalle_receta.html'

class AppointmentDetailView(DetailView):
    model = Cita
    context_object_name = 'cita'
    template_name = 'citas/cita_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(AppointmentDetailView, self).get_context_data(**kwargs)
        context.update({
            'anotacion_form': AnotacionForm, # get the form instance
            'receta_form': RecetaForm
        })

        return context

class AppointmentCreate(TemplateView):
    template_name = 'citas/crear_cita.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['id'] = kwargs['pk']
        context['name'] = kwargs['name']
        return context

class SearchResultsListView(ListView):
    ''' Resultados de busqueda '''
    model = Paciente
    context_object_name = 'pacients'
    template_name = "search_result.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Paciente.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) |
            Q(correo__icontains=query) |
            Q(telefono__icontains=query) |
            Q(telefono_emergencia__icontains=query) |
            Q(correo__icontains=query) 
        )

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('q')
        context['citas'] =  Cita.objects.filter(
            Q(paciente__nombre__icontains=query) |
            Q(paciente__telefono__icontains=query) |
            Q(paciente__telefono_emergencia__icontains=query) |
            Q(comentario__icontains=query) |
            Q(paciente__correo__icontains=query) 
        )

        return context