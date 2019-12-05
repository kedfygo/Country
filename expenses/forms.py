from django import forms
from .models import Expenses
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TextInput, NumberInput

class ExpensesForm(forms.ModelForm):
    
    class Meta:
        model = Expenses
        fields = ('date', 'folio', 'provider', 'description', 'amount', 'notes')
 
        widgets = {
            'date': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Fecha'}),
            'folio': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Número de Folio'}),
            'provider': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Proveedor'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Descripción'}),
            'amount': NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Monto del Gasto'}),
            'notes': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Observaciones Adicionales'}),
        }


