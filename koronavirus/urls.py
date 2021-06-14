from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graf/', views.graf, name='graf'),
    path('staty/<int:pk>/', views.StatDetailView.as_view(), name='stat_detail'),
    path('staty/create/', views.StatCreateView.as_view(), name='stat_create'),
    path('staty/<int:pk>/update/', views.StatUpdateView.as_view(), name='stat_update'),
    path('staty/<int:pk>/delete/', views.StatDeleteView.as_view(), name='stat_delete'),
]
