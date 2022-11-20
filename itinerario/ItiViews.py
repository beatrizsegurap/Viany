from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def dash(request):
    return render(request, 'itinerario/paso1.html')


def dash2(request):
    return render(request, 'itinerario/paso2.html')


def resumen(request):
    return render(request, 'itinerario/resumen.html')


def escanear(request):
    return render(request, 'itinerario/escanear.html')


def listar(request):
    return render(request, 'itinerario/listar.html')