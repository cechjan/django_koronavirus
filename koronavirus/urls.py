from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graf/', views.graf, name='graf'),
    path('staty/<int:pk>/', views.StatDetailView.as_view(), name='stat_detail'),
]
