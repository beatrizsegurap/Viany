from django.shortcuts import render,redirect
from .hospedajes import TIPO_HOSPEDAJE
from .forms import FormIngresarHospedaje
from .models import hospedaje_por_dia
from django.http import HttpResponse

# Create your views here.

def hospedaje (request):

    model = hospedaje_por_dia.objects.filter(id_itinerario_id__exact = int(request.session["id_itinerario"]))
    context= {'lodging':model}

    return render(request,"hospedaje.html",context)

def agregarHospedaje (request):
    if request.method == 'POST':
        form = FormIngresarHospedaje(request.POST or None)

        if form.is_valid():

            form.save()
            form = FormIngresarHospedaje()

        return redirect("/hospedaje/menu/")

    id_itineario = request.session["id_itinerario"]

    return render(request,'agregar-hospedaje.html', {'idItinerario':id_itineario, 'tiposH':TIPO_HOSPEDAJE})

def eliminarHospedaje (request, id_hospedaje):

    hpj= hospedaje_por_dia.objects.get(pk=id_hospedaje)
    hpj.delete()

    model = hospedaje_por_dia.objects.filter(id_itinerario_id__exact = int(request.session["id_itinerario"]))
    context= {'lodging':model}

    return render(request,"hospedaje.html",context)
