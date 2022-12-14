from django.shortcuts import render
from .transportes import TIPOS_TRANSPORTE
from .ciudades import CIUDADES

# Create your views here.

def transporte (request):
    return render(request, 'transporte.html')

def agregarTransporte (request):
    return render(request, 'agregar-transporte.html',{'tiposT':TIPOS_TRANSPORTE, 'ciudades':CIUDADES})
