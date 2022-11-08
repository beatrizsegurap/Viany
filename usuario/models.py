from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100,null=False,verbose_name='nombre')
    nombre_cuenta_usuario = models.CharField(max_length=20,null=False,verbose_name='nickname')
    correo_usuario = models.CharField(max_length=50,null=False,verbose_name='mail')
    contraseña_usuario = models.CharField(max_length=20,null=False,verbose_name='contraseña')
    direccion_usuario = models.CharField(null=True,max_length=100,verbose_name='direccion')
    telefono_usuario = models.IntegerField(null=True,verbose_name='telefono')

