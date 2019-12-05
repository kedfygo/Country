from django.urls import path
from . import views
from .views import PaymentsListView, PaymentsDetailView, PaymentsCreate

paymentspatterns = ([
    path('', PaymentsListView.as_view(), name='payments'),
    path('<int:pk>/', PaymentsDetailView.as_view(), name='payment'),
    path('create/', PaymentsCreate.as_view(), name='create')
], 'payments')
