from django.shortcuts import render

# Create your views here.

def transporte (request):
    return render(request, 'transporte.html')

def agregarTransporte (request):
    return render(request, 'agregar-transporte.html')
