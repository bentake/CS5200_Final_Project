from django import forms
from .models import Customer, Vehicle, Subscription, ParkingRecord, Staff, Vehicle
from django.forms import inlineformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'street', 'city', 'state', 'zip']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'make', 'model', 'year', 'type', 'fuel_type']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['lot', 'license_plate', 'price', 'time_start', 'time_end']
        widgets = {
            'time_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'time_end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ParkingRecordForm(forms.ModelForm):
    class Meta:
        model = ParkingRecord
        fields = ['license_plate', 'lot', 'spot', 'time_entered']
        widgets = {
            'time_entered': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'name', 'shift_start', 'shift_end', 'lot']


