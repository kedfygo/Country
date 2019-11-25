from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments_list, name='payments'),
    path('add-payment/', views.add_payment, name='add-payment')
]
