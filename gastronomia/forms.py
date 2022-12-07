from django import forms
from .models import gastronomia_por_dia

class formAddGastronomia(forms.ModelForm):
    class Meta:
        model = gastronomia_por_dia
        fields = ['detalle_gastronomia', 'hora_inicio_gastronomia', 'hora_final_gastronomia', 'valor_total_gastronomia', 'fecha_gastronomia']