from django.shortcuts import render,redirect
from .models import Paciente
from .forms import pacienteForm
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
