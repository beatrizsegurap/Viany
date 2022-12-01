from django.shortcuts import render,redirect
from .hospedajes import TIPOS_HOSPEDAJE

# Create your views here.

def hospedaje (request):
    return render(request,'hospedaje.html')

def agregarHospedaje (request):
    return render(request,'agregar-hospedaje.html',{'tiposH':TIPOS_HOSPEDAJE})