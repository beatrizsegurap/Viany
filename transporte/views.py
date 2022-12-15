from django.shortcuts import render, redirect
from .transportes import TIPOS_TRANSPORTE
from .cities import COMUNAS_CHILE
from .forms import FormIngresarTransporte

# Create your views here.

def transporte (request):
    numeroDias=[]
    i=1
    for cantDias in request.session['lista_dias']:
        numeroDias.append(i)
        i= int(cantDias) + i 

    res = dict(zip(request.session['lista_destinos'], numeroDias))
    ciudad_origen = request.session['ciudad_origen_itinerario']

    return render(request, 'transporte.html', {'destinos': res, 'origen' : ciudad_origen})

def agregarTransporte (request):

    # if request.method == 'POST':
    #     form = FormIngresarTransporte(request.POST or None)
    #     id_itineario_id = request.session["id_itinerario"]
    #     if form.is_valid:
    #         form.save()
    #         form = FormIngresarTransporte()

    #     return redirect("/transporte/menu/")
    res = dict(zip(request.session['lista_destinos'], request.session['lista_dias']))
    return render(request, 'agregar-transporte.html',{'tiposT': TIPOS_TRANSPORTE, 'ciudades': COMUNAS_CHILE, 'destinos': res})

