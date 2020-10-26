from django.shortcuts import render,redirect
from .models import Paciente
from cita.models import Cita,Receta
from anotacion.models import Anotacion
from examen.models import Examen
from .forms import pacienteForm
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf 

# Create your views here.
# def listado_pacientes(request):
#     pacientes=Paciente.objects.all()
#     contexto = {'paciente':pacientes}
#     return render(request, 'users/listado_pacientes.html',contexto)

def listado_pacientes(request):
    pacientes=Paciente.objects.all()
    data={
        'lista_pacientes':pacientes
    }
    return render(request, 'users/listado_pacientes.html',data)

def modificar_paciente(request,correo): #con este parametro correo haces la busqueda en la bd y obtenes
    paciente = Paciente.objects.get(correo=correo) # el paciente que va a modificar
    if request.method == 'GET':
        form = pacienteForm(instance=paciente)
    else:
        form = pacienteForm(request.POST,instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('listado_pacientes')
    return render(request,'paciente/ingresar_paciente.html', {'form': form})
    #return render(request,'home.html')  #aca cambiale el home.html por la pagina de modificar

def ingresar_paciente(request):
    form = pacienteForm(request.POST)
    #if request.method == 'POST':
    if form.is_valid():
        form.save()
        #return redirect('pages:listado_pacientes')
        pacientes=Paciente.objects.all()
        data={
            'lista_pacientes':pacientes
        }
        return render(request, 'users/listado_pacientes.html',data)

    else:
        form = pacienteForm()
    return render(request, 'paciente/ingresar_paciente.html', {'form': form})
    
    #form = pacienteForm(request.POST or None)
   # if form.is_valid():
   #     form.save()
   #     form = pacienteForm()
   # context = {
   #     'form': form
   # }
   # return render(request, "paciente/ingresar_paciente.html", context)


def detalle_paciente(request, correo):
    paciente = Paciente.objects.get(correo=correo)
    if request.method == 'GET':
        form = pacienteForm(instance=paciente)
    return render(request,'paciente/detalle_paciente.html',{'form':form})

class reporte_historial_clinico(View):
    def get(self, request, *args, **kwargs):
        template =  get_template('paciente/reporte_pacientes.html')
        data = {
             'Pacientes':Paciente.objects.all(),
             'Citas':Cita.objects.all(),
             'Anotaciones':Anotacion.objects.all(),
             'Recetas':Receta.objects.all(),
             'Examenes':Examen.objects.all(),
        }
        pdf = render_to_pdf('paciente/reporte_pacientes.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def reporte_historial_clinicoPaciente(request,id):

    template =  get_template('paciente/reporte_paciente.html')
    paciente = Paciente.objects.get(pk=id)
    citas = Cita.objects.filter(paciente=paciente)
    data = {
        'Pacientes':paciente,
        'Citas':citas,
        'Anotaciones':Anotacion.objects.all(),
        'Recetas':Receta.objects.all(),
        'Examenes':Examen.objects.all(),
    }
    pdf = render_to_pdf('paciente/reporte_paciente.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def g_get_labels(val):
    if val == 0:
        return ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    else:
        return ["ERROR"]
