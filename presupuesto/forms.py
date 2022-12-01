from django import forms
from .models import presupuesto

class formAct(forms.ModelForm):
    class Meta:
        model = presupuesto
        fields = ['nombre_item_presupuesto','precio_item_presupuesto']