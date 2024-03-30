# farmer/booking/forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time']  # เลือกฟิลด์ที่ต้องการให้ driver กรอก

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'วันที่'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'เวลา'})
