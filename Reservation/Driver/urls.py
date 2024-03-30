#Driver/urls.py
from django.urls import path
from .views import*

urlpatterns = [
    path('home_driver/', home_driver, name='home_driver'),  # Provide a unique path for the driver home
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    
]
