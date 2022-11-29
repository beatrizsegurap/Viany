from django import forms
from django.db import models
from .models import itinerario

class FormCreateItinerario(forms.ModelForm):
    class Meta:
        model = itinerario
        fields = ('nombre_itinerario','fecha_inicio_itinerario')
