from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formAddGastronomia
from .models import gastronomia_por_dia


# Create your views here.

def gastronomia(request): 

    model = gastronomia_por_dia.objects.filter(id_itinerario_id__exact = int(request.session["id_itinerario"]) )
    context = {'gastronomy':model}
    return render(request,"gastronomia.html",context)

def agregarGastronomia(request):
    if request.method == 'POST':
        form = formAddGastronomia(request.POST or None)
        if form.is_valid():

            form.save()
            form = formAddGastronomia()

        return redirect("/gastronomia/menu/")
        
    id_itineario = request.session["id_itinerario"]
    
    return render(request,'agregar-gastronomia.html',{'idItinerario':id_itineario})

def eliminarGastronomia(request, id_gastronomia):

    Egastronomia= gastronomia_por_dia.objects.get(pk = id_gastronomia)
    Egastronomia.delete()

    gastronomia = gastronomia_por_dia.objects.all()

    return render(request,"gastronomia.html",{"gastronomia_por_dia":gastronomia})
