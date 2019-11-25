from django.shortcuts import render,redirect
from .models import Providers
from .forms import ProvidersForm

# Create your views here.
def providers_list(request): 
    providers_listed = Providers.objects.all()
    context = {
        'providers_listed' : providers_listed,
    }
    return render(request, 'providers/providers.html', context)

def add_provider(request):
    if request.method == "POST":
        form = ProvidersForm(request.POST)
        if form.is_valid():
          provider = form.save()
          return redirect('providers')
    else:
        form = ProvidersForm()
    context = {
        'form' : form,
    }
    return render(request, 'providers/add-provider.html', context)
"""
def add_provider(request):
    form = ProvidersForm()
    context = {
        'form' : form,
    }
    return render(request, 'providers/add-provider.html')
"""
"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
"""