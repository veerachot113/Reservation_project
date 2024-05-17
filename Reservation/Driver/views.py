#Driver/urls.py
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from Accounts.models import *
#เพิ่มรถ
@login_required
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
    return render(request, 'Driver/add_vehicle.html', {'form': form})


@login_required
def add_detailvehicle(request, id=None):  # เพิ่มพารามิเตอร์ id และกำหนดค่าเริ่มต้นเป็น None
    if id is not None:  # ตรวจสอบว่ามี id ที่ส่งมาหรือไม่
        try:
            vehicle = Vehicle.objects.get(pk=id)
        except Vehicle.DoesNotExist:
            return redirect('home_driver')  

        if request.method == 'POST':
            form = DetailvehicleForm(request.POST)
            if form.is_valid():
                detail_vehicle = form.save(commit=False)
                detail_vehicle.vehicle = vehicle  
                detail_vehicle.save()
                return redirect('home_driver')  
        else:
            form = DetailvehicleForm()
        return render(request, 'Driver/add_detailvehicle.html', {'form': form, 'vehicle': vehicle})
    else:
        return redirect('home_driver')  # ถ้าไม่มี id ส่งมาให้ redirect กลับไปยังหน้าหลักของ driver



