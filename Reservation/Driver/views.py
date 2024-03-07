#Driver/urls.py
from django.shortcuts import render, redirect
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from Accounts.models import UserDriver


@login_required
def home_driver(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'Driver/home_driver.html',{'vehicles': vehicles})


@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            # ตรวจสอบค่าที่เลือกจากฟอร์มและกำหนดให้กับฟิลด์ province ของโมเดล
            vehicle.province = request.POST['province']
            vehicle.driver = request.user  # กำหนดคนขับรถเป็นผู้ใช้ที่ล็อกอินอยู่
            vehicle.save()
            return redirect('add_vehicle')  # หรือไปยังหน้าอื่นๆ ตามที่คุณต้องการ
    else:
        form = VehicleForm()
    return render(request, 'driver/add_vehicle.html', {'form': form})

# @login_required
# def add_vehicle(request):
#     if request.method == 'POST':
#         form = VehicleForm(request.POST, request.FILES)
#         if form.is_valid():
#             vehicle = form.save(commit=False)
#             driver = UserDriver.objects.get(pk=request.user.id)
#             vehicle.driver = driver  # กำหนด driver เป็นอ็อบเจกต์ของคนขับที่เข้าสู่ระบบ
#             vehicle.save()
#             return redirect('home_driver')  # หรือไปยัง URL ที่คุณต้องการ
#     else:
#         form = VehicleForm(initial={'driver': request.user}) 
#     return render(request, 'driver/add_vehicle.html', {'form': form, 'driver_name': request.user.get_full_name()})


