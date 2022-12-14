from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User



class hospedaje_por_dia(models.Model):
    id_hospedaje =  models.AutoField(primary_key=True)
    id_itinerario = models.ForeignKey("itinerario.itinerario", on_delete=models.CASCADE)
    tipo_hospedaje = models.CharField(max_length=20,null=False,verbose_name="tipo hospedaje")
    nombre_hospedaje = models.CharField(max_length=30,null=False,verbose_name="nombre hospedaje")
    valor_total_hospedaje = models.IntegerField(null=False,verbose_name="valor total")
    direccion_hospedaje  =  models.CharField(max_length=50,null=False,verbose_name="direccion hospedaje")
    fecha_hospedaje = models.DateField(verbose_name="fecha")
    numero_camas = models.IntegerField(null=False,verbose_name="numero camas")
