from django.shortcuts import render
from .models import Providers

# Create your views here.
def providers_list(request): 
    providers_listed = Providers.objects.all()
    context = {
        'providers_listed' : providers_listed,
    }
    return render(request, 'providers/providers.html', context)

def add_provider(request):
    return render(request, 'providers/add-provider.html')