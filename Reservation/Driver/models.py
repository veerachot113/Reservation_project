#Driver/models.py
from django.db import models

from Accounts.models import UserDriver  # import UserDriver model from accounts app

class Vehicle(models.Model):
    driver = models.OneToOneField(UserDriver, on_delete=models.CASCADE, related_name='vehicles')  # Add related_name='vehicles'
    
    model = models.CharField(max_length=200)
    TYPE_CHOICES = (
        ('แบบรองกระสอบ', 'แบบรองกระสอบ'),
        ('แบบถังอุ้ม', 'แบบถังอุ้ม'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    price = models.CharField(max_length=20)
    province = models.CharField(max_length=200)
    image = models.ImageField(upload_to='vehicle_images/')

    def __str__(self):
        return self.model
