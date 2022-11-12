from django import forms
from django.db import models
from .models import check_list

class FormIngresarHospedaje(forms.ModelForm):
    class Meta:
        model = check_list
        fields = ('nombre_item_checklist', 'estado_item_checklist')