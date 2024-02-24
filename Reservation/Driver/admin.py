#Driver/admin.py
from django.contrib import admin
from .models import*
from django.utils.html import format_html

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'driver', 'model', 'type', 'price', 'province']

    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>', obj.image.url)

admin.site.register(Vehicle, VehicleAdmin)