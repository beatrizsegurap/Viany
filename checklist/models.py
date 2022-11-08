from tabnanny import verbose
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class check_list(models.Model):
    id_checklist =  models.AutoField(primary_key=True)
    id_itinerario = models.ForeignKey("itinerario.itinerario", on_delete=models.CASCADE)
    nombre_item_checklist = models.CharField(max_length=50,null=False,verbose_name="nombre item")
    estado_item_checklist = models.BooleanField(null=False,verbose_name="estado item")
