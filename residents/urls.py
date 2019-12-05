from django.urls import path
from . import views
from .views import ResidentsListView, ResidentsDetailView, ResidentsCreate, ResidentsUpdate, ResidentsDelete


residents_patterns = ([
    path('', ResidentsListView.as_view(), name='residents'),
    path('<int:pk>/', ResidentsDetailView.as_view(), name='resident'),
    path('create/', ResidentsCreate.as_view(), name='create'),
    path('update/<int:pk>/', ResidentsUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ResidentsDelete.as_view(), name='delete'),
], 'residents')
