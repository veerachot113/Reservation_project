# farmer/booking/models.py
from django.db import models
from Accounts.models import UserFarmer 

from Driver.models import *
class Booking(models.Model):
    name = models.ForeignKey(UserFarmer,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=500,null=True,blank=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True,blank=True)  # เพิ่มชื่อ-สกุล
    address = models.TextField()  # เพิ่มที่อยู่
    quantity = models.IntegerField()#เพิ่มจำนวนไร่
    phone = models.CharField(max_length=15, default='')  # เพิ่มเบอร์โทรศัพท์
    details = models.TextField() 
    TYPE_CHOICES = (
        ('รออนุมัติ', 'รออนุมัติ'),
        ('อนุมัติแล้ว', 'อนุมัติแล้ว'),
        ('ไม่อนุมัติ', 'ไม่อนุมัติ'),
        ('กำลังดำเนินการ', 'กำลังดำเนินการ'),
        ('เสร็จสิ้น', 'เสร็จสิ้น'),
        ('ยกเลิก', 'ยกเลิก'),
    )
    status = models.CharField(max_length=100, choices=TYPE_CHOICES,default='รออนุมัติ')
    





# from django.db import models
# from accounts.models import UserFarmer  # แก้ไขนี้

# class Farmer(models.Model):
#     user = models.OneToOneField(
#         UserFarmer,  # แก้ไขนี้
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     address = models.CharField(max_length=255)
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return f'Farmer: {self.user.name}'

