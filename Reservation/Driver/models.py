#Driver/models.py
from django.db import models
from Accounts.models import UserDriver  # import UserDriver model from Accounts app

class Vehicle(models.Model):
    driver = models.OneToOneField(UserDriver, on_delete=models.CASCADE, related_name='vehicles')  # Add related_name='vehicles'
    model = models.CharField(max_length=100, verbose_name='รุ่น')
    TYPE_CHOICES = (
        ('แบบรองกระสอบ', 'แบบรองกระสอบ'),
        ('แบบถังอุ้ม', 'แบบถังอุ้ม'),
    )
    type = models.CharField(max_length=100,verbose_name='ประเภทรถ', choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='ราคา')
    province = models.CharField(max_length=200, verbose_name='จังหวัดที่ลงพื้นที่')
    image = models.ImageField(upload_to='vehicle_images/',null=True, blank=True, verbose_name='รูปภาพรถ')

    def __str__(self):
        return self.model


