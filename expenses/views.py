from django.shortcuts import render, redirect
from .models import Expenses
from django.template import loader
from .forms import ExpensesForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
class ExpensesListView(ListView):
    model = Expenses

class ExpensesDetailView(DetailView):
    model = Expenses

class ExpensesCreate(CreateView):
    model = Expenses
    form_class = ExpensesForm
    success_url = reverse_lazy('expenses:expenses')

def expenses_list(request):
    expenses_listed = Expenses.objects.all()
    context = {
        'expenses_listed' : expenses_listed,
    }
    return render(request, 'expenses/expenses.html', context)

def add_expense(request):
    if request.method == "POST":
        form = ExpensesForm(request.POST)
        if form.is_valid():
          expense = form.save()
          return redirect('expenses')
    else:
        form = ExpensesForm()
    context = {
        'form' : form,
    }
    return render(request, 'expenses/add-expense.html', context)


