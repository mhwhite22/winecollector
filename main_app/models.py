from django.db import models
from django.urls import reverse
from datetime import date

class Distributor(models.Model):
  name = models.CharField(max_length=50)
  place = models.CharField(max_length=30)

  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('distributors_detail', kwargs={'pk': self.id })

  
class Wine(models.Model):  # Note that parens are optional if not inheriting from another class
  name = models.CharField(max_length=100)
  region = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  vintage = models.IntegerField()
  distributor = models.ManyToManyField(Distributor)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'wine_id': self.id })

class Tasting(models.Model):
  date = models.DateField()
  note = models.CharField(max_length=200, default="No Notes")
  wine = models.ForeignKey(Wine, on_delete=models.CASCADE)


  class Meta: 
    ordering = ['-date']
