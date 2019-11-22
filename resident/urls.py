from django.urls import path

from . import views

urlpatterns = [
    path('', views.residents_list, name='residents_list'),
]