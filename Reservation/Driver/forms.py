# Driver/forms.py
from django import forms
from .models import Vehicle,Detailvehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['image', 'model', 'type', 'price', 'province']


class DetailvehicleForm(forms.ModelForm):
    class Meta:
        model = Detailvehicle
        fields = ['power', 'details']