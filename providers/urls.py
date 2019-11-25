from django.urls import path
from . import views

urlpatterns = [
    path('', views.providers_list, name='providers'),
    path('add-provider/', views.add_provider, name='add-provider'),
    ]