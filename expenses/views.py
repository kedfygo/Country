from django.shortcuts import render
from .models import Expenses
from django.template import loader

# Create your views here.
def expenses_list(request):
    expenses_listed = Expenses.objects.all()
    context = {
        'expenses_listed' : expenses_listed,
    }
    return render(request, 'expenses/expenses.html', context)

def add_expense(request):
    return render(request, 'expenses/add-expense.html')
