# booking/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from Driver.models import Vehicle
from django.utils.decorators import method_decorator
from .forms import BookingForm
from django.views import View

@login_required
def create_booking(request, vehicle_id):
    if not request.user.groups.filter(name='farmer').exists():
        return redirect('home')  # หรือหน้าที่ต้องการให้ driver หรือผู้ที่ไม่ได้เป็น farmer ไป

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.farmer = request.user
            booking.vehicle = vehicle
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form, 'vehicle': vehicle})




class BookingListView(View):
    @method_decorator(login_required)
    def get(self, request):
        is_driver = request.user.groups.filter(name='driver').exists()
        if is_driver:
            bookings = Booking.objects.filter(vehicle__driver=request.user)
        else:
            bookings = Booking.objects.filter(farmer=request.user)
        return render(request, 'booking/booking_list.html', {'bookings': bookings, 'is_driver': is_driver})

class BookingApprovalView(View):
    @method_decorator(login_required)
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.vehicle.driver != request.user:
            action = request.POST.get('action')
            if action == 'approve':
                booking.status = 'อนุมัติแล้ว'
                booking.vehicle.driver = request.user
                booking.appointment_date = request.POST.get('appointment_date')
            elif action == 'reject':
                booking.status = 'ไม่อนุมัติ'
            booking.save()
        return redirect('booking_list')
