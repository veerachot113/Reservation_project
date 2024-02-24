#Driver/urls.py
from django.urls import path
from .views import*

urlpatterns = [
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
]
