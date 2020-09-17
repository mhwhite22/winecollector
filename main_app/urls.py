from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wines/', views.wines_index, name='index'),
    path('wines/<int:wine_id>/', views.wines_detail, name='detail'),
    path('wines/create/', views.WineCreate.as_view(), name='wines_create'),
    path('wines/<int:pk>/update/', views.WineUpdate.as_view(), name='wines_update'),
    path('wines/<int:pk>/delete/', views.WineDelete.as_view(), name='wines_delete'),
    path('wines/<int:pk>/add_tasting/', views.add_tasting, name='add_tasting'),
    
]