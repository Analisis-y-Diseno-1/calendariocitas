from django.shortcuts import render
from cita.models import Cita
from .models import Examen
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ExaminationForm
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Create your views here.
#def ExaminationCreate(request, pk):

#    return HttpResponseRedirect('/citas/'+pk)

class ExaminationCreate(DetailView):
    model = Cita
    context_object_name = 'cita'
    template_name = 'examen/examination_create_form.html'
    
    def get_form(self):
        form = self.form_class(instance=ExaminationForm)
        return form
    
    def get_context_data(self, **kwargs):
        context = super(ExaminationCreate, self).get_context_data(**kwargs)
        context.update({
            'examination_form': ExaminationForm
        })

        return context

def ExaminationActionCreate(request, pk):
    form = ExaminationForm(request.POST)
    print(pk)
    if form.is_valid():
        print("Si entro")
        examen = form.save(commit=False)
        #fecha = datetime.now()
        cita = Cita.objects.get(pk=pk)
        examen.cita = cita
        print(examen.descripcion)
        examen.save()

    return HttpResponseRedirect('/crear_examen/'+pk)

def ExaminationListView():
    pass