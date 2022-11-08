from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class presupuesto(models.Model):
    id_presupuesto =  models.AutoField(primary_key=True)
    id_itinerario = models.ForeignKey("itinerario.itinerario", on_delete=models.CASCADE)
    nombre_item_presupuesto = models.CharField(max_length=50,null=False,verbose_name="nombre item")
    precio_item_presupuesto = models.IntegerField(null=False,verbose_name="precio item")
