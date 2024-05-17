# booking/models.py
from django.utils import timezone  
from django.db import models
from Driver.models import Vehicle
from Accounts.models import *



class Booking(models.Model):
    STATUS_CHOICES = [
        ('รออนุมัติ', 'รออนุมัติ'),
        ('อนุมัติแล้ว', 'อนุมัติแล้ว'),
        ('ไม่อนุมัติ', 'ไม่อนุมัติ'),
    ]

    farmer = models.ForeignKey(UserFarmer, on_delete=models.CASCADE, related_name='bookings',default='')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    address = models.TextField()
    quantity = models.IntegerField()
    phone = models.CharField(max_length=15)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='รออนุมัติ')
    appointment_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Booking by {self.farmer.username} for {self.vehicle.model}'
