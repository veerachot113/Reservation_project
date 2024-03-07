from django.urls import path,include
from .views import *
urlpatterns = [
    path('home_farmer/', home_farmer, name='home_farmer'),# Provide a unique path for the farmer home
    path('booking/<int:id>/',booking, name='booking'),
    path('showbooking/',showbooking, name='showbooking'),

 
]