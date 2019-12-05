from django.shortcuts import redirect
from .models import Providers
from .forms import ProvidersForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
class ProvidersListView(ListView):
    model = Providers

class ProvidersDetailView(DetailView):
    model = Providers

class ProvidersCreate(CreateView):
    model = Providers
    form_class = ProvidersForm
    success_url = reverse_lazy('providers:providers')

class ProvidersUpdate(UpdateView):
    model = Providers
    form_class = ProvidersForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('providers:update', args=[self.object.register_id]) + '?ok' 

class ProvidersDelete(DeleteView):
    model = Providers
    success_url = reverse_lazy('providers:providers')    

