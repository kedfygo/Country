from django.shortcuts import render, redirect
from .models import Residents
from django.template import loader
from .forms import ResidentsForm

# Create your views here.
def residents_list(request):
    residents_listed = Residents.objects.all()
    context = {
        'residents_listed' : residents_listed,
    }
    return render(request, 'residents/residents.html', context)

def add_resident(request):
    if request.method == "POST":
        form = ResidentsForm(request.POST)
        if form.is_valid():
          resident = form.save()
          return redirect('residents')
    else:
        form = ResidentsForm()
    context = {
        'form' : form,
    }
    return render(request, 'residents/add-resident.html', context)
