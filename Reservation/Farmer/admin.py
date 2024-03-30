#Farmer/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_vehicle_image', 'name', 'display_name_driver', 'vehicle_type', 'quantity', 'address', 'details', 'phone', 'status']

    def display_vehicle_image(self, obj):
        if obj.vehicle:
            return format_html('<img src="{}" width="100" height="100"/>', obj.vehicle.image.url)
        else:
            return None
        
    def display_name_driver(self, obj):
        if obj.vehicle:
            return obj.vehicle.driver.name
        else:
            return None

    display_vehicle_image.short_description = 'Vehicle Image'

admin.site.register(Booking, BookingAdmin)

