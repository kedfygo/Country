from django.shortcuts import render, redirect
from .models import Resident
from django.template import loader
from .forms import ResidentForm

# Create your views here.
def residents_list(request):
    residents_listed = Resident.objects.all()
    context = {
        'residents_listed' : residents_listed,
    }
    return render(request, 'resident/residents.html', context)

def add_resident(request):
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
          resident = form.save()
          return redirect('residents')
    else:
        form = ResidentForm()
    context = {
        'form' : form,
    }
    return render(request, 'resident/add-resident.html', context)
