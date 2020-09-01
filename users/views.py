from django.shortcuts import render
from .models import Paciente
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
