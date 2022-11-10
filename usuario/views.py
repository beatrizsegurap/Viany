from django.shortcuts import render,redirect
from .forms import FormRegisterUser, FormLoginUser
from django.http import HttpResponse
from django.contrib import messages
from .models import usuario

# Create your views here.
def index (request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        try:
            acceso = usuario.objects.get(correo_usuario = request.POST['correo_usuario'],contraseña_usuario = request.POST['contraseña_usuario'])
            print("usuario=",acceso.nombre_usuario)
            request.session['correo_usuario']=acceso.correo_usuario
            request.session['nombre_usuario']=acceso.nombre_usuario
            return render(request, 'dashboard-user.html')
        except usuario.DoesNotExist as e:
            messages.success(request, 'Los datos ingresados no son correctos')
    return render(request, 'login.html')

def cerrarSesion(request):
    try:
        del request.session['nombre_usuario']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')

def dashboarduser(request):
    return render(request, 'dashboard-user.html')



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