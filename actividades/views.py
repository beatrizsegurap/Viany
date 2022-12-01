from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formAct

# Create your views here.

def actividades(request):
    return render(request,"actividad.html")

def agregarActividad (request):
    
    return render(request,'agregar-actividad.html')
        