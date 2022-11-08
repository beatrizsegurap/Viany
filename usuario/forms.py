from django import forms
from django.db import models
from .models import usuario



class FormRegisterUser(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('nombre_usuario', 'nombre_cuenta_usuario','correo_usuario','contraseña_usuario')
