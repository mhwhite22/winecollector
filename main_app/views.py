from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Wine, Distributor
from .forms import TastingForm
# Create your views here.

class WineCreate(CreateView):
    model = Wine
    fields = ['name', 'region', 'description', 'vintage']

class WineUpdate(UpdateView):
    model = Wine
    fields = ['region', 'description', 'vintage', ]

class WineDelete(DeleteView):
    model = Wine
    success_url = '/wines/'

def home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    wines = Wine.objects.all()
    return render(request, 'wines/index.html', { 'wines': wines})

def wines_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    distributor_wine_doesnt_have = Distributor.objects.exclude(id__in = wine.distributor.all().values_list('id'))
    tasting_form = TastingForm()
    return render(request, 'wines/detail.html', {
        'wine': wine,
        'tasting_form': tasting_form,
        'distributor': distributor_wine_doesnt_have
        })

def add_tasting(request, wine_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit=False)
        new_tasting.wine_id = wine_id
        new_tasting.save()
    return redirect('detail', wine_id=wine_id)

def assoc_distributor(request, wine_id, distributor_id):
    Wine.objects.get(id=wine_id).distributors.add(distributor_id)
    return redirect('detail', wine_id=wine_id)

class DistributorList(ListView):
  model = Distributor

class DistributorDetail(DetailView):
  model = Distributor

class DistributorCreate(CreateView):
  model = Distributor
  fields = '__all__'

class DistributorUpdate(UpdateView):
  model = Distributor
  fields = ['name', 'place']

class DistributorDelete(DeleteView):
  model = Distributor
  success_url = '/distributors/'