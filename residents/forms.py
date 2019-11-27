from django import forms
from .models import Residents
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TextInput

class ResidentsForm(forms.ModelForm):
    
    class Meta:
        model = Residents
        fields = ('name', 'lastname', 'address', 'phone_number', 'email', 'type_of_property', 'owner_name', 'owner_phone_number')
 
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Residente'}),
            'lastname': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Apellido del Residente'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Calle y Número de Casa'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Número Telefónico del Residente'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Correo electrónico del residente'}),
            'type_of_property': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tipo de Propiedad'}),
            'owner_name': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Propietario'}),
            'owner_phone_number': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Número Telefónico del Propietario'}),
        }


