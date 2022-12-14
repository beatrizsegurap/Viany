from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url, register
from django.views.decorators.csrf import csrf_protect
from .forms import FormCreateItinerario1, FormDestinos
from .models import itinerario
from .cities import COMUNAS_CHILE
# Create your views here.

# @register.filter()
# def range(min=0):
#     return range(min)

def crearItinerario(request):
    comunas = COMUNAS_CHILE
    if request.method == 'POST':
        form = FormCreateItinerario1(request.POST or None)
        if form.is_valid():
            id_registro = form.save()

            request.session['id_itinerario'] = id_registro.id_itinerario
            #print(form.data.get('nombre_itinerario'),form.data.get('ciudad_origen_itinerario'),form.data.get('fecha_inicio_itinerario'))
            request.session['nombre_itinerario'] = form.data.get('nombre_itinerario')
            request.session['ciudad_origen_itinerario'] = form.data.get('ciudad_origen_itinerario')
            request.session['fecha_inicio_itinerario'] = form.data.get('fecha_inicio_itinerario')
            form = FormCreateItinerario1()
            return redirect('/itinerario/agregardestinos')
  
    return render(request, 'itinerario/paso1.html',{'comunas':comunas})



def agregarDestinos(request):
    comunas = COMUNAS_CHILE
    if request.method == 'POST':
        request.session['lista_destinos'] = request.POST.getlist('destino[]')
        request.session['lista_dias'] = request.POST.getlist('dia_destino[]')
        formD = FormDestinos(request.POST or None)
        return redirect('/itinerario/resumen')

    return render(request, 'itinerario/agregardestinos.html',{'comunas':comunas})


def resumen(request):
    #for key, value in request.session.items():
    #    print(key, value)
    #    print(request.session['lista_destinos'])
  

    res = dict(zip(request.session['lista_destinos'], request.session['lista_dias']))

    return render(request, 'itinerario/resumen.html', {'destinos': res})


def misItinerarios(request):
    return render(request, 'itinerario/listar.html')