from django.urls import path
from .views import ProvidersListView, ProvidersDetailView, ProvidersCreate, ProvidersUpdate, ProvidersDelete

providers_patterns = ([
    path('', ProvidersListView.as_view(), name='providers'),
    path('<int:pk>/', ProvidersDetailView.as_view(), name='provider'),
    path('update/<int:pk>/', ProvidersUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProvidersDelete.as_view(), name='delete'),
    path('create/', ProvidersCreate.as_view(), name='create'),
    ], 'providers')