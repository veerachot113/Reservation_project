#Farmer/admin.py
from .models import*
from django.contrib import admin
from django.utils.html import format_html

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'fullname','display_vehicle_image','display_name_driver','address', 'quantity', 'phone', 'details']

    def display_vehicle_image(self, obj):
        if obj.vehicle:
            return format_html('<img src="{}" width="100" height="100"/>', obj.vehicle.image.url)
        else:
            return None
        
    def display_name_driver(self,obj):
        return obj.vehicle.driver
    display_vehicle_image.short_description = 'Vehicle Image'

admin.site.register(Booking, BookingAdmin)
