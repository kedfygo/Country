from django.shortcuts import render
from django.http import HttpResponse
from .models import Resident
from django.template import loader

# Create your views here.
def residents_list(request):
    residents_listed = Resident.objects.all()
    context = {
        'residents_listed' : residents_listed,
    }
    return render(request, 'resident/residents.html', context)


