from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from anotacion.models import Anotacion
from anotacion.forms import AnotacionForm
from django.urls import reverse_lazy
from datetime import datetime 

# Create your views here.

def crear_anotacion(request):
    return render(request,'anotacion/index.html')


#class annotationCreate(CreateView):
#    model = Anotacion
#    form_class = AnotacionForm
#    template_name = 'anotacion/anotacion_form.html'

#    def post(self, request, *args, **kwargs):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/success/')
#        return render(request, self.template_name, {'form': form})

def annotationCreate(request, fk):
    form = AnotacionForm(request.POST)
    
    if form.is_valid():
        anotacion = form.save(commit=False)
        fecha = datetime.now()
        anotacion.fecha_hora = fecha
        anotacion.id_cita = fk
        anotacion.save()

        #return HttpResponseRedirect('/success/')
        return HttpResponseRedirect(reverse('/anotacion/'))

    else:
        print ("ERROR")
        return render(request,'anotacion/index.html')