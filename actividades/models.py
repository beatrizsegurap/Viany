from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class actividad_por_dia(models.Model):
    id_actividad =  models.AutoField(primary_key=True)
    id_itinerario = models.ForeignKey("itinerario.itinerario", on_delete=models.CASCADE)
    detalle_actividad = models.CharField(max_length=50,null=False,verbose_name="detalle actividad")
    hora_inicio_actividad = models.TimeField(null=False,verbose_name="hora inicio")
    hora_final_actividad = models.TimeField(null=False,verbose_name="hora final")
    valor_total_actividad = models.IntegerField(null=False,verbose_name="valor total")
    fecha_actividad = models.DateField(verbose_name="fecha")
