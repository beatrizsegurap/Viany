from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class transporte_por_dia(models.Model):
    id_transporte =  models.AutoField(primary_key=True)
    id_itinerario = models.ForeignKey("itinerario.itinerario", on_delete=models.CASCADE)
    tipo_de_transporte = models.CharField(max_length=20,null=False,verbose_name="tipo transporte")
    hora_salida_transporte = models.TimeField(null=False,verbose_name="hora salida")
    hora_llegada_transporte = models.TimeField(null=False,verbose_name="hora llegada")
    valor_total_transporte = models.IntegerField(null=False,verbose_name="valor total")
    ciudad_inicio_transporte = models.CharField(max_length=20,null=False,verbose_name="ciudad origen")
    ciudad_destino_transporte  =  models.IntegerField(null=False,verbose_name="ciudad destino")
    fecha_transporte = models.DateField(verbose_name="fecha")
