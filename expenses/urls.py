from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_list, name='expenses'),
    path('expenses/add-expense/', views.add_expense, name='add-expense'),
]
