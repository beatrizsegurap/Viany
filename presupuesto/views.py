from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formAct

# Create your views here.

def presupuesto(request):
    return render(request,"presupuesto.html")
