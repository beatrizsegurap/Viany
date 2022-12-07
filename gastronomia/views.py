from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formAct

# Create your views here.

def gastronomia(request):
    if request.method == 'POST':
        form = formAddGastronomia(request.POST or None)
        if form.is_valid():
            form.save()
            request.session['fecha_gastronomia'] = form.data.get('fecha_gastronomia')
            request.session['detalle_gastronomia'] = form.data.get('detalle_gastronomia')
            request.session['hora_inicio_gastronomia'] = form.data.get('hora_inicio_gastronomia')
            request.session['hora_final_gastronomia'] = form.data.get('hora_final_gastronomia')
            request.session['valor_total_gastronomia'] = form.data.get('valor_total_gastronomia')
            form = formAddGastronomia()
    return redirect("/gastronomia/menu")

def agregarGastronomia(request):
    return render(request,'agregar-gastronomia.html')
