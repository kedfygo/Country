from django import forms
from .models import Residents
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TextInput, ChoiceField, RadioSelect

class ResidentsForm(forms.ModelForm):
    
    class Meta:
        model = Residents
        fields = ('name', 'lastname', 'address', 'phone_number', 'email', 'type_of_property', 'owner_name', 'owner_phone_number')
 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Residente'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Apellido del Residente'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Calle y Número de Casa'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Número Telefónico del Residente'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Correo electrónico del residente'}),
            'type_of_property': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tipo de Propiedad'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Propietario'}),
            'owner_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Número Telefónico del Propietario'}),
        }


