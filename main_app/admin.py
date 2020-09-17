from django.contrib import admin
from .models import Wine, Tasting

# Register your models here.

admin.site.register(Wine),
admin.site.register(Tasting)
