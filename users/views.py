from django.shortcuts import render
from .models import Paciente
from .forms import pacienteForm
# Create your views here.
def listado_pacientes(request):
    pacientes=Paciente.objects.all()
    data={
        'lista_pacientes':pacientes
    }
    return render(request, 'users/listado_pacientes.html',data)

def modificar_paciente(request,correo): #con este parametro correo haces la busqueda en la bd y obtenes
                                        # el paciente que va a modificar
    return render(request,'home.html')  #aca cambiale el home.html por la pagina de modificar

def ingresar_paciente(request):
    form = pacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = pacienteForm()
    context = {
        'form': form
    }
    return render(request, "paciente/ingresar_paciente.html", context)
    #form = AnotacionForm(request.POST)
    #return render(request, 'paciente/ingresar_paciente.html', {'form': form})
    #return render(request, "paciente/ingresar_paciente.html")