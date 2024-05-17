# booking/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['fullname', 'address', 'quantity', 'phone', 'details']

class BookingUpdateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status', 'appointment_date']