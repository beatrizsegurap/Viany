from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from usuario.models import usuario
from .cities import REGIONES_CHILE,PROVINCIAS_CHILE,COMUNAS_CHILE

class itinerario(models.Model):
    id_itinerario =  models.AutoField(primary_key=True)
   # casilla = models.ForeignKey("casillaItinerario", on_delete=models.CASCADE)
    nombre_itinerario = models.CharField(max_length=20,null=False,verbose_name="nombre itinerario")
    ciudad_origen_itinerario = models.CharField(max_length=20,null=False,verbose_name="ciudad origen")
    fecha_inicio_itinerario = models.DateField(null=False,verbose_name="fecha inicio")
    cant_dias_itinerario = models.IntegerField(verbose_name="cantidad dias")
    ciudad_destino_itinerario = models.CharField(max_length=20,null=False,verbose_name="ciudad destino")
    id_publico_itinerario =  models.IntegerField(verbose_name="id publico")
    publica_privada_itinerario = models.BooleanField(verbose_name="permiso")


class casillaItinerario(models.Model):
    id_casilla = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey("usuario.usuario", on_delete=models.CASCADE)
    id_itinerario = models.ForeignKey("itinerario", on_delete=models.CASCADE)
    propietario_itinerario = models.CharField(max_length=20,null=False,verbose_name="propietario")


    
