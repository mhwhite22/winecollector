from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Wine:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, region, description, vintage):
    self.name = name
    self.region = region
    self.description = description
    self.vintage = vintage

wines = [
  Wine('Martin Muellen Riesling Revival', 'Mosel, Germany', 'Dry classic Riesling', 2016),
  Wine('Championship Bottle Hard Promises', 'Willamette, Oregon', 'Dry, racy Pinot Blanc', 2018),
]

def home(request):
    return HttpResponse('Hi this is winecollector')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    return render(request, 'wines/index.html', { 'wines': wines})