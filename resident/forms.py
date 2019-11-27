from django import forms
from .models import Resident
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TextInput

class ResidentForm(forms.ModelForm):
    
    class Meta:
        model = Resident
        fields = ('name', 'lastname', 'address', 'email', 'type_of_property', 'owner_name')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Residente'}),
            'lastname': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Apellido del Residente'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Calle y Número de Casa'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Correo electrónico del residente'}),
            'type_of_property': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tipo de Propiedad'}),
            'owner_name': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Propietario'}),
        }


