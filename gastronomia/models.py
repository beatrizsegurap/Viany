from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class gastronomia_por_dia(models.Model):
    id_gastronomia =  models.AutoField(primary_key=True)
    id_itinerario = models.ForeignKey("itinerario.itinerario", on_delete=models.CASCADE)
    detalle_gastronomia = models.CharField(max_length=50,null=False,verbose_name="detalle gastronomia")
    hora_inicio_gastronomia = models.TimeField(null=False,verbose_name="hora inicio")
    hora_final_gastronomia = models.TimeField(null=False,verbose_name="hora final")
    valor_total_gastronomia = models.IntegerField(null=False,verbose_name="valor total")
    fecha_gastronomia = models.DateField(verbose_name="fecha")

    def str(self):
        return self.name
