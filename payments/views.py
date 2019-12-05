from django.shortcuts import render, redirect
from .models import Payments
from django.template import loader
from .forms import PaymentsForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
class PaymentsListView(ListView):
    model = Payments

class PaymentsDetailView(DetailView):
    model = Payments

class PaymentsCreate(CreateView):
    model = Payments
    form_class = PaymentsForm
    success_url = reverse_lazy('payments:payments')


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
