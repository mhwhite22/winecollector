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
    path('wines/<int:wine_id>/add_tasting/', views.add_tasting, name='add_tasting'),
    path('wines/<int:wine_id>/assoc_distributor/<int:distributor_id>/', views.assoc_distributor, name='assoc_distributor'),
    path('distributors/', views.DistributorList.as_view(), name='distributors_index'),
    path('distributors/<int:pk>/', views.DistributorDetail.as_view(), name='distributors_detail'),
    path('distributors/create/', views.DistributorCreate.as_view(), name='distributors_create'),
    path('distributors/<int:pk>/update/', views.DistributorUpdate.as_view(), name='distributors_update'),
    path('distributors/<int:pk>/delete/', views.DistributorDelete.as_view(), name='distributors_delete'),
    
]