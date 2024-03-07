#farmerbooling/views
from django.shortcuts import render, redirect
from Driver.models import *
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def home_farmer(request):
    vehicles = Vehicle.objects.all()
    return render(request,'Farmer/home_farmer.html',{'vehicles': vehicles})
def booking(request, id):
    if not request.user.is_authenticated or not request.user.groups.filter(name='farmer').exists():
        return redirect('home_driver')  # หรือไปยัง URL ที่คุณต้องการให้ผู้ใช้กลับไปหน้าเดิมหากไม่ใช่ farmer หรือไม่ได้เข้าสู่ระบบ
    
    vehicles = Vehicle.objects.get(pk=id)
    if request.method == 'POST':
        name = request.user
        fullname = request.POST.get('fullname')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        phone = request.POST.get('phone')
        details = request.POST.get('details')
    
        b = Booking.objects.create(
            name=name,
            fullname=fullname,
            address=address,
            quantity=quantity,
            phone=phone,
            details=details,
            vehicle=vehicles
        )
        b.save()
        return redirect('home_driver')  # หรือไปยัง URL ที่คุณต้องการ
   
    return render(request, 'Farmer/booking.html', {'vehicles': vehicles})


def showbooking(request):
    if not request.user.is_authenticated or not request.user.groups.filter(name='farmer').exists():
        return redirect('showbooking')  # หรือไปยัง URL ที่คุณต้องการให้ผู้ใช้กลับไปหน้าเดิมหากไม่ใช่ farmer หรือไม่ได้เข้าสู่ระบบ
    
    booking = Booking.objects.filter(name=request.user)
    return render(request, 'Farmer/showbooking.html', {'booking': booking})


def booking_success(request):
    return render(request, 'booking_success.html')



