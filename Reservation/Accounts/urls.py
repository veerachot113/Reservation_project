# Accounts/urls.py
from django.contrib import *
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_accounts, name='home'),
    path('logout/', custom_logout, name='logout'),
    path('userlogin/', user_login, name='login'),#หน้าlogin
    path('registerfarmer/', register_farmer, name='registerfarmer'),#หน้าสมัครเป็นfarmer
    path('registerdriver/', register_driver, name='registerdriver'),#หน้าสมัครเป็นdriver
    path('useregister/', useregister, name='chooserole'),#หน้าสำหรับเลือกบทบาทว่าเป็น farmer หรือ driver
    path('profile/update/', profile_update, name='profile_update'),
    path('driver-profile/<int:driver_id>/', view_driver_profile, name='view_driver_profile'),

]


