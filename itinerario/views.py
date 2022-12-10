from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import url, register
from django.views.decorators.csrf import csrf_protect
from .forms import FormCreateItinerario1, FormCreateItinerario, FormCasilla
from .models import itinerario,casillaItinerario
from usuario.models import usuario
from .cities import COMUNAS_CHILE
import random
from datetime import timedelta,datetime


# Create your views here.

@register.filter()

#Creamos id para compartir de tamaño 8
def id_compartida():
    id = ''
    for cod in range(8):
       id = id + str(random.choice(list(range(10))))
    return int(id)

#calculamos el total de dias que durará el viaje
def calcular_dias(dias):
    total=0
    for i in range(len(dias)):
        total+=int(dias[i])
    return total

#Diccionario con el destino y la cantidad de dias
def total_destinos(destinos,dias):
    dict_destinos = dict()
    for i in range(len(destinos)):
        dict_destinos[destinos[i]]=dias[i]
    return dict_destinos

def planificacion(inicio,destinos,dias):
    total = dict()
    inicio = datetime.strptime(inicio, '%Y-%m-%d')
    for i in range(len(destinos)):
        for j in range(int(dias[i])):
            total[str(inicio).split()[0]]= destinos[i]
            inicio = inicio + timedelta(days=1)
    return total

def crearItinerario(request):
    comunas = COMUNAS_CHILE
    if request.method == 'POST':
        form = FormCreateItinerario1(request.POST or None)
        if form.is_valid():
            request.session['nombre_itinerario'] = form.data.get('nombre_itinerario')
            request.session['ciudad_origen_itinerario'] = form.data.get('ciudad_origen_itinerario')
            request.session['fecha_inicio_itinerario'] = form.data.get('fecha_inicio_itinerario')    
            return redirect('/itinerario/agregardestinos')
  
    return render(request, 'itinerario/paso1.html',{'comunas':comunas})



def agregarDestinos(request):
    comunas = COMUNAS_CHILE
    if request.method == 'POST':
        itinerario = planificacion(request.session['fecha_inicio_itinerario'],request.POST.getlist('destino[]'),request.POST.getlist('dia_destino[]'))
        request.session['itinerario'] = itinerario
        request.session['id_publica_itinerario'] = id_compartida()
        request.session['cant_dias_itinerario'] = calcular_dias(request.POST.getlist('dia_destino[]'))
        return redirect('/itinerario/resumen')

    return render(request, 'itinerario/agregardestinos.html',{'comunas':comunas})


def resumen(request):
    cas = casillaItinerario(propietario_itinerario=request.session['id_usuario'], id_usuario=usuario.objects.get(request.session['id_usuario']))
    cas.save()
    it = itinerario(nombre_itinerario = request.session['nombre_itinerario'], ciudad_origen_itinerario = request.session['ciudad_origen_itinerario'],fecha_inicio_itinerario =request.session['fecha_inicio_itinerario'], cant_dias_itinerario=request.session['cant_dias_itinerario'])
    dias = request.session['itinerario']
    return render(request, 'itinerario/resumen.html',{'dias':dias})


def misItinerarios(request):
    return render(request, 'itinerario/listar.html')