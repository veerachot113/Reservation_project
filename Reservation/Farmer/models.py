# farmer/booking/models.py
from django.db import models
from Accounts.models import*
from Driver.models import Vehicle

class Booking(models.Model):
    name = models.ForeignKey(UserFarmer, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=500, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField()
    quantity = models.IntegerField()
    phone = models.CharField(max_length=15, default='')
    details = models.TextField() 
   
    vehicle_type = models.CharField(max_length=100, verbose_name='ประเภทรถ', default='')
    TYPE_CHOICES = (
        ('รออนุมัติ', 'รออนุมัติ'),
        ('อนุมัติแล้ว', 'อนุมัติแล้ว'),
        ('ไม่อนุมัติ', 'ไม่อนุมัติ'),
        ('กำลังดำเนินการ', 'กำลังดำเนินการ'),
        ('เสร็จสิ้น', 'เสร็จสิ้น'),
        ('ยกเลิก', 'ยกเลิก'),
    )
    status = models.CharField(max_length=100, choices=TYPE_CHOICES, default='รออนุมัติ')

