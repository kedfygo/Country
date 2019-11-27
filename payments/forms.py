from django import forms
from .models import Payments
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, TextInput

class PaymentsForm(forms.ModelForm):
    
    class Meta:
        model = Payments
        fields = ('name', 'lastname', 'address', 'description', 'amount', 'type_of_payment', 'proof_of_payment', 'date_of_payment')
 
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nombre del Residente'}),
            'lastname': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Apellido del Residente'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Calle y Número de Casa'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Descripción del Pago'}),
            'amount': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Monto del pago'}),
            'type_of_payment': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tipo de pago'}),
            'proof_of_payment': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Comprobante de Pago'}),
            'date_of_payment': TextInput(attrs={'class': 'form-control', 'placeholder' : 'Fecha de pago'}),
        }



