from django.shortcuts import render, redirect
from .models import Residents
from django.template import loader
from .forms import ResidentsForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
class ResidentsListView(ListView):
    model = Residents

class ResidentsDetailView(DetailView):
    model = Residents

class ResidentsCreate(CreateView):
    model = Residents
    form_class = ResidentsForm
    success_url = reverse_lazy('residents:residents')

class ResidentsUpdate(UpdateView):
    model = Residents
    form_class = ResidentsForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('residents:update', args=[self.object.id]) + '?ok'   

class ResidentsDelete(DeleteView):
    model = Residents
    success_url = reverse_lazy('residents:residents')    
    