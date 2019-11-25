from django.shortcuts import render
from .models import Payments
from django.template import loader

# Create your views here.

def payments_list(request): 
    payments_listed = Payments.objects.all()
    context = {
        'payments_listed' : payments_listed,
    }
    return render(request, 'payments/payments.html', context)

def add_payment(request):
    return render(request, 'payments/add-payment.html')




