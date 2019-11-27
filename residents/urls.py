from django.urls import path
from . import views

urlpatterns = [
    path('', views.residents_list, name='residents'),
    path('add-resident/', views.add_resident, name='add-resident'),
]
