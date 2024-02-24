from django.urls import path,include
from .views import *
urlpatterns = [
    path('booking/<int:id>/',booking, name='booking'),
    path('showbooking/',showbooking, name='showbooking'),

 
]