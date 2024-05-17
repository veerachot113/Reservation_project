# booking/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('create_booking/<int:vehicle_id>/', create_booking, name='create_booking'),  # URL สำหรับการสร้างการจอง โดยรับพารามิเตอร์ vehicle_id
    path('booking_list/', BookingListView.as_view(), name='booking_list'),  # URL สำหรับดูรายการการจอง
    path('booking_approval/<int:booking_id>/', BookingApprovalView.as_view(), name='booking_approval'),  # URL สำหรับการอนุมัติหรือปฏิเสธการจอง โดยรับพารามิเตอร์ booking_id
]