#Driver/urls.py
from django.urls import path
from .views import*

urlpatterns = [
    # Provide a unique path for the driver home
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    path('add_detailvehicle/', add_detailvehicle, name='add_detailvehicle'),

    
]
