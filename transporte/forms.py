from django import forms
from django.db import models
from .models import transporte_por_dia

class FormIngresarTransporte(forms.ModelForm):
    class Meta:
        model = transporte_por_dia
        fields = ('tipo_de_transporte', 'hora_salida_transporte', 'hora_llegada_transporte', 
        'valor_total_transporte', 'ciudad_inicio_transporte', 'ciudad_destino_transporte', 'fecha_transporte')
