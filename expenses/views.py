from django.shortcuts import render, redirect
from .models import Expenses
from django.template import loader
from .forms import ExpensesForm

# Create your views here.
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


