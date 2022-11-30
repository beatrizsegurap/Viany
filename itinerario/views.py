from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url
from django.views.decorators.csrf import csrf_protect
from .forms import FormCreateItinerario1, FormDestinos
from .models import itinerario
from .cities import COMUNAS_CHILE
# Create your views here.


def crearItinerario(request):
    comunas = COMUNAS_CHILE
    if request.method == 'POST':
        form = FormCreateItinerario1(request.POST or None)
        if form.is_valid():
            form.save()
            print(form.data.get('nombre_itinerario'),form.data.get('ciudad_origen_itinerario'),form.data.get('fecha_inicio_itinerario'))
            form = FormCreateItinerario1()
            return redirect('/itinerario/paso2')
  
    return render(request, 'itinerario/paso1.html',{'comunas':comunas})



def agregarDestinos(request):
    comunas = COMUNAS_CHILE
    if request.method == 'POST':
        formD = FormDestinos(request.POST or None)
        print(request.POST['destino'])
        return redirect('/itinerario/resumen')

    return render(request, 'itinerario/paso2.html',{'comunas':comunas})


def resumen(request):
    return render(request, 'itinerario/resumen.html')



def misItinerarios(request):
    return render(request, 'itinerario/listar.html')