from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import FormCreateItinerario
from .cities import COMUNAS_CHILE
# Create your views here.


def crearItinerario(request):
    comunas = COMUNAS_CHILE
    return render(request, 'itinerario/paso1.html',{'comunas':comunas})



def agregarDestinos(request):
    comunas = COMUNAS_CHILE

    return render(request, 'itinerario/paso2.html',{'comunas':comunas})


def resumen(request):
    return render(request, 'itinerario/resumen.html')



def listar(request):
    return render(request, 'itinerario/listar.html')