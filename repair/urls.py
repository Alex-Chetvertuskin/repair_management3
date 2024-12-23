from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devices/', views.devices, name='devices'),
    path('clients/', views.clients, name='clients'),
    path('repairs/', views.repairs, name='repairs'),
]
