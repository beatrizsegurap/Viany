from django import forms
from django.db import models
from .models import itinerario

class FormCreateItinerario1(forms.ModelForm):
    class Meta:
        model = itinerario
        fields = ('nombre_itinerario','ciudad_origen_itinerario','fecha_inicio_itinerario')

class FormDestinos(forms.Form):
    cant_dias_itinerario = forms.CharField()
    destinos_itinerario = forms.IntegerField()
    



