from django.urls import path
from . import views
from .views import ExpensesListView, ExpensesCreate, ExpensesDetailView

expensespatterns = ([
    path('', ExpensesListView.as_view(), name='expenses'),
    path('create/', ExpensesCreate.as_view(), name='create'),
    path('<int:pk>/', ExpensesDetailView.as_view(), name='expense'),
], 'expenses')
