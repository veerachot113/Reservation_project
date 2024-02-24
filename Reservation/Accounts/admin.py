# Accounts/admin.py
from django.contrib import admin
from .models import UserFarmer, UserDriver

class UserFarmerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_farmer', 'is_driver']  # สังเกตุได้ที่ 'is_farmer', 'is_driver'

admin.site.register(UserFarmer, UserFarmerAdmin)

class UserDriverAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',  'first_name', 'last_name','is_farmer', 'is_driver']  # สังเกตุได้ที่ 'is_farmer', 'is_driver'

admin.site.register(UserDriver, UserDriverAdmin)