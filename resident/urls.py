from django.urls import path
from . import views

urlpatterns = [
    path('residents/', views.residents_list, name='residents'),
    path('providers/', views.providers_list, name='providers'),
    path('expenses/', views.expenses, name='expenses'),
    path('add-resident/', views.add_resident, name='add-resident'),
    path('payments/', views.payments, name='payments')
]
