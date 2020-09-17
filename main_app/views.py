from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wine
from .forms import TastingForm
# Create your views here.

class WineCreate(CreateView):
    model = Wine
    fields = '__all__'

class WineUpdate(UpdateView):
    model = Wine
    fields = ['region', 'description', 'vintage', ]

class WineDelete(DeleteView):
    model = Wine
    success_url: '/wines/'

def home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    wines = Wine.objects.all()
    return render(request, 'wines/index.html', { 'wines': wines})

def wines_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    return render(request, 'wines/detail.html', {'wine': wine})

def add_tasting(request, wine_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit=False)
        new_tasting.wine_id = wine_id
        new_tasting.save()
    return redirect('detail', wine_id=wine_id)


