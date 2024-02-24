#Driver/urls.py
from django.shortcuts import render, redirect
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from Accounts.models import UserDriver

@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            # ดึงข้อมูลคนขับจากโมเดล UserDriver ที่เข้าสู่ระบบ
            driver = UserDriver.objects.get(pk=request.user.id)
            vehicle.driver = driver  # กำหนด driver เป็นอ็อบเจกต์ของคนขับที่เข้าสู่ระบบ
            vehicle.save()
            return redirect('home_driver')  # หรือไปยัง URL ที่คุณต้องการ
    else:
        form = VehicleForm()
    return render(request, 'Driver/add_vehicle.html', {'form': form})

