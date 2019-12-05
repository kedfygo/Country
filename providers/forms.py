from django import forms
from .models import Providers
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TextInput

class ProvidersForm(forms.ModelForm):
    
    class Meta:
        model = Providers
        fields = ('description', 'rfc', 'address', 'category', 'phone', 'email')
        
        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Razón Social'}),
            'rfc': TextInput(attrs={'class': 'form-control', 'placeholder' : 'RFC del Proveedor'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Calle y Número del local'}),
            'category': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Producto o Servicio / Ramo'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Número de Teléfono'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Dirección de correo electrónico'}),
        }


