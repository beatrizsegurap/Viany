from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formAct

# Create your views here.

def gastronomia(request):
    return render(request,"gastronomia.html")

def agregarGastronomia(request):
    render(request,'agregar-gastronomia.html')
