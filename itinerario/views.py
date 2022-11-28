from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect



# Create your views here.


def crearItinerario(request):
    return render(request, 'itinerario/paso1.html')



def agregarDestinos(request):
    if request.method != 'POST':
        return redirect('/itinerario/nuevo')
    return render(request, 'itinerario/paso2.html')


def resumen(request):
    return render(request, 'itinerario/resumen.html')



def listar(request):
    return render(request, 'itinerario/listar.html')