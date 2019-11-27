from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_list, name='expenses'),
    path('add-expense/', views.add_expense, name='add-expense'),
]
