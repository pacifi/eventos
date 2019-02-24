from django import forms
from .models import Acceso


class AccesoModelForm(forms.ModelForm):
    class Meta:
        model = Acceso
        exclude = ()
