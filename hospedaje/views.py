from django.shortcuts import render

# Create your views here.

def hospedaje (request):
    return render(request,'hospedaje.html')

def agregarHospedaje (request):
    return render(request,'agregar-hospedaje.html')