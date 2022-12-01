from django import forms
from .models import actividad_por_dia

class formAct(forms.ModelForm):
    class Meta:
        model = actividad_por_dia
        fields = ['detalle_actividad', 'hora_inicio_actividad', 'hora_final_actividad', 'valor_total_actividad', 'fecha_actividad']