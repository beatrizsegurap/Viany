from django.shortcuts import render,redirect
from .forms import FormRegisterUser
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def index (request):
    return render(request,'index.html')

def login(request):
    return render(request, 'login.html')

def dashboarduser(request):
    return render(request, 'dashboard-user.html',data)



def signup(request):
    form = FormRegisterUser(request.POST or None)
    if form.is_valid():
        form.save()		
        messages.success(request, 'Usuario registrado exitosamente.')
        form = FormRegisterUser()
    else:
        messages.error(request, 'Error al registrar usuario.')
    context = {'form': form }      
    return render(request, 'sign-up.html', context)