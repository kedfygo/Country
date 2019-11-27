from django.shortcuts import render, redirect
from .models import Payments
from django.template import loader
from .forms import PaymentsForm

# Create your views here.

def payments_list(request): 
    payments_listed = Payments.objects.all()
    context = {
        'payments_listed' : payments_listed,
    }
    return render(request, 'payments/payments.html', context)

def add_payment(request):
    if request.method == "POST":
        form = PaymentsForm(request.POST)
        if form.is_valid():
          payment = form.save()
          return redirect('residents')
    else:
        form = PaymentsForm()
    context = {
        'form' : form,
    }

    return render(request, 'payments/add-payment.html', context)
