#Driver/views.py
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from Accounts.models import *
from Booking.models import *
from django.shortcuts import render, redirect, get_object_or_404


#เพิ่มรถ
@login_required
def add_vehicle(request):
    no_of_pending_request = count_pending_rent_request(request.user)
    existing_vehicle = Vehicle.objects.filter(driver=request.user).first()
    if request.method == 'POST':
        if existing_vehicle:
            form = VehicleForm(request.POST, request.FILES, instance=existing_vehicle)
        else:
            form = VehicleForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.instance.driver = request.user
            form.save()
            return redirect('home_driver')
    else:
        if existing_vehicle:
            form = VehicleForm(instance=existing_vehicle)
        else:
            form = VehicleForm()
    
    return render(request, 'Driver/add_vehicle.html', {
        'form': form,
        'existing_vehicle': existing_vehicle,
        'no_of_pending_request': no_of_pending_request
    })

@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, driver=request.user)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('home_driver')
    return render(request, 'Driver/confirm_delete.html', {'vehicle': vehicle})

def count_pending_rent_request(driver):
    no_of_pending_request = 0
    bookings = Booking.objects.filter(vehicle__driver=driver)
    for booking in bookings:
        if booking.request_status == "Pending":
            no_of_pending_request += 1
    return no_of_pending_request


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



# def count_pending_rent_request(driver):
#     no_of_pending_request = 0
#     bookings = Booking.objects.filter(vehicle__driver=driver)
#     for booking in bookings:
#         if booking.request_status == "Pending":
#             no_of_pending_request += 1
#     return no_of_pending_request
 

     
