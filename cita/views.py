from django.shortcuts import render
from .models import Cita, Receta
from .forms import recetaOffForm
from django.contrib import messages
from django.shortcuts import redirect
from users.models import Paciente
from .forms import RecetaForm
from datetime import datetime 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

def appointment_update(request, pk):
    query = request.POST
    if Cita.objects.filter(id=pk).exists():
        try:
            cita = Cita.objects.get(id=pk)
            cita.fecha_cita=query['fecha_cita']
            cita.hora_cita=query['hora_cita']
            cita.comentario=query['comentario']

            cita.save()
        except:
            messages.add_message(request, messages.ERROR, 
            'ERROR: Ha ocurrido un error al actualizar la cita, intenta de nuevo.')
        else:
            messages.add_message(request, messages.INFO, 
            '¡Hemos guardado tus cambios!')
            
    return redirect('cita_detail', pk=pk)

def appointment_create(request, pk):
    query = request.POST
    try:
        cita = Cita(
            fecha_cita=query['fecha_cita'],
            hora_cita=query['hora_cita'],
            comentario=query['comentario'],
            paciente=Paciente.objects.get(id=pk),
        )
        cita.save()
        send_mail(
            'Receta',
            "{0}, para el dia {1} a la hora {2}".format(
                cita.comentario,
                cita.fecha_cita,
                cita.hora_cita
            ),
            'medsistemnotify@gmail.com',
            [cita.paciente.correo],
            fail_silently=False,
        )
    except:
        messages.add_message(request, messages.ERROR, 
        'ERROR: Ha ocurrido un error al crear la cita, intenta de nuevo.')
    else:
        messages.add_message(request, messages.INFO, 
        '¡Hemos guardado tus cambios!')
        
            
    return redirect('crear_cita', pk=pk, name=Paciente.objects.get(id=pk).nombre)


def appointment_delete(request, pk):
    query = request.POST
    if Cita.objects.filter(id=pk).exists():
        try:
            cita = Cita.objects.get(id=pk)
            cita.delete()
        except:
            messages.add_message(request, messages.ERROR, 
            'ERROR: Ha ocurrido un error al eliminar la cita, intenta de nuevo.')
        else:
            messages.add_message(request, messages.INFO, 
            '¡Se ha eliminado la cita!')
            
    return redirect('citas')

def appointment_serve(request, pk):
    query = request.POST
    if Cita.objects.filter(id=pk).exists():
        try:
            cita = Cita.objects.get(id=pk)
            cita.estado="ATENDIDA"
            cita.save()
        except:
            messages.add_message(request, messages.ERROR, 
            'ERROR: Ha ocurrido un error al atender la cita, intenta de nuevo.')
        else:
            messages.add_message(request, messages.INFO, 
            '¡Se ha atendido la cita!')
            
    return redirect('citas')


def RecetaCreate(request, id):
    form = RecetaForm(request.POST)
    
    if form.is_valid():
        receta = form.save(commit=False)
        #fecha = datetime.now()
        cita = Cita.objects.get(id=id)
        receta.cita = cita
        receta.save()
        
        send_mail(
            'Receta',
            receta.detalle_receta,
            'medsistemnotify@gmail.com',
            [receta.cita.paciente.correo],
            fail_silently=False,
        )



    return HttpResponseRedirect('/citas/'+id)

def ingresar_receta_off(request):
    form = recetaOffForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('recetas')
    else:
        form = recetaOffForm()
    return render(request, 'citas/crear_receta_off.html', {'form': form})

def eliminar_receta(request,id):
    receta = Receta.objects.get(pk=id)
    receta.delete()
    return redirect('recetas')
	

