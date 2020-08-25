from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def crear_anotacion(request):
    return render(request,'anotacion/index.html')
