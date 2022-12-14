from django import forms
from django.db import models
from .models import hospedaje_por_dia

class FormIngresarHospedaje(forms.ModelForm):
    class Meta:
        model = hospedaje_por_dia
        fields = ('tipo_hospedaje', 'nombre_hospedaje','valor_total_hospedaje','direccion_hospedaje','fecha_hospedaje','id_itinerario','numero_camas')
