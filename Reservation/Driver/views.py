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





from Accounts.models import UserDriver  # Import UserDriver model from Accounts app

def add_vehicle(request):
    if request.method == 'POST':
        try:
            # ตรวจสอบว่ามีรถของผู้ใช้งานที่เข้าสู่ระบบอยู่แล้วหรือไม่
            vehicle = Vehicle.objects.get(driver=request.user)
            form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        except Vehicle.DoesNotExist:
            # ถ้ายังไม่มีให้สร้างรถใหม่
            form = VehicleForm(request.POST, request.FILES)
            
        if form.is_valid():
            form.instance.driver = request.user
            form.save()
            return redirect('home_driver')
    else:
        # ดึงข้อมูลรถล่าสุดของผู้ใช้งานที่เข้าสู่ระบบ
        latest_vehicle = Vehicle.objects.filter(driver=request.user).order_by('-id').first()
        initial_data = {}
        if latest_vehicle:
            initial_data = {
                'image': latest_vehicle.image,
                'model': latest_vehicle.model,
                'type': latest_vehicle.type,
                'price': latest_vehicle.price,
                'province': latest_vehicle.province,
            }
        form = VehicleForm(initial=initial_data)
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


