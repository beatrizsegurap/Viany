from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formAddActividad
from .models import actividad_por_dia

# Create your views here.

def actividades(request):

    model = actividad_por_dia.objects.filter(id_itinerario_id__exact = int(request.session["id_itinerario"]) )
    context = {'activities':model}

    return render(request,"actividad.html",context)

def agregarActividad (request):
    if request.method == 'POST':
        form = formAddActividad(request.POST or None)

        if form.is_valid():

            form.save()
            form = formAddActividad()

        return redirect("/actividades/menu/")

    id_itineario = request.session["id_itinerario"]

    return render(request,'agregar-actividad.html',{'idItinerario':id_itineario})

def eliminarActividad(request, id_actividad):

    Eactividad= actividad_por_dia.objects.get(pk = id_actividad)
    Eactividad.delete()

    model = actividad_por_dia.objects.filter(id_itinerario_id__exact = int(request.session["id_itinerario"]) )
    context = {'activities':model}

    return render(request,"actividad.html",context)