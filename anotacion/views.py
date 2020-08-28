from django.shortcuts import render
from django.http import HttpResponse
from .models import Anotacion
from .forms import CardAnotacion_form
# Create your views here.

def crear_anotacion(request):
    return render(request,'anotacion/anotacion_form.html')

def listado_anotaciones(request):
    anotaciones=Anotacion.objects.all()
    data={
        'lista_anotaciones':anotaciones
    }
    return render(request, 'anotacion/listado_anotaciones.html',data)

def modificar_anotacion(request,id):
    anotacion=Anotacion.objects.get(no_anotacion=id) 
    data = {
        'form': CardAnotacion_form(instance=anotacion)
    }
    if request.method=="POST":
        formulario=CardAnotacion_form(data=request.POST, instance=anotacion)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Anotacion modificada correctamente"
            data['form'] = formulario
    return render(request, 'anotacion/modificar_anotacion.html',data)