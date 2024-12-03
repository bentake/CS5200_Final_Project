from django.shortcuts import render
from .models import Customer, ParkingLot, ParkingRecord, Vehicle, Subscription, BillingRecord, Staff
from django.db.models import Sum
from django.db import connection
from django.db.models import Max, F
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CustomerForm, VehicleForm, SubscriptionForm, ParkingRecordForm, StaffForm
from django.db.models import Prefetch
from django.shortcuts import render
from .models import Customer
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            last_customer = Customer.objects.last()
            if last_customer:
                new_customer_id = last_customer.customer_id + 1
            else:
                new_customer_id = 1
            
            customer = form.save(commit=False)
            customer.customer_id = new_customer_id
            
            customer.save()

            messages.success(request, 'Customer created successfully.')
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form, 'action': 'Create'})

def customer_update(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully.')
            return redirect('customer_detail', customer_id=customer_id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form, 'action': 'Update'})

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    if request.method == 'POST':
        Vehicle.objects.filter(customer=customer).delete()
        customer.delete()
        messages.success(request, 'Customer and associated vehicles deleted successfully.')
        return redirect('customer_list')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})

def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription created successfully.')
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscription_form.html', {'form': form, 'action': 'Create'})

def subscription_update(request, subscription_id):
    subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription updated successfully.')
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)
    return render(request, 'subscription_form.html', {'form': form, 'action': 'Update'})

def subscription_delete(request, subscription_id):
    subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
    if request.method == 'POST':
        subscription.delete()
        messages.success(request, 'Subscription deleted successfully.')
        return redirect('subscription_list')
    return render(request, 'subscription_confirm_delete.html', {'subscription': subscription})

def dashboard(request):
    total_customers = Customer.objects.count()
    total_vehicles = Vehicle.objects.count()
    total_lots = ParkingLot.objects.all()
    active_parkings = ParkingRecord.objects.filter(time_left__isnull=True).count()
    
    context = {
        'total_customers': total_customers,
        'total_vehicles': total_vehicles,
        'parking_lots': total_lots,
        'active_parkings': active_parkings,
    }
    return render(request, 'dashboard.html', context)

def parking_status(request, lot_id=None):
    parking_lots = ParkingLot.objects.all()
    
    if lot_id:
        lot = ParkingLot.objects.get(lot_id=lot_id)
        current_parkings = ParkingRecord.objects.filter(
            lot=lot,
            time_left__isnull=True
        ).select_related('license_plate', 'spot')
        
        occupied_spots = lot.number_of_spots - lot.available_spots
        lot.occupancy_rate = round((occupied_spots / lot.number_of_spots) * 100) if lot.number_of_spots > 0 else 0
        
    else:
        lot = None
        current_parkings = ParkingRecord.objects.filter(
            time_left__isnull=True
        ).select_related('license_plate', 'spot', 'lot')
    
    context = {
        'lot': lot,
        'current_parkings': current_parkings,
        'parking_lots': parking_lots,
    }
    return render(request, 'parking_status.html', context)

def customer_list(request):
    customers = Customer.objects.prefetch_related('vehicles').all()
    return render(request, 'customer_list.html', {'customers': customers})


def parked_vehicles_with_subscription(request, lot_id):
    parked_vehicles = ParkingRecord.objects.filter(
        lot_id=lot_id,
        time_left__isnull=True
    ).annotate(
        subscription_end=Max(F('license_plate__subscription__time_end'))
    ).filter(
        subscription_end__gte=timezone.now()
    ).select_related('license_plate', 'spot')
    
    context = {
        'parked_vehicles': parked_vehicles
    }
    return render(request, 'parking_status.html', context)

def subscription_parking_history(request, subscription_id):
    parking_history = ParkingRecord.objects.filter(
        license_plate__subscription__subscription_id=subscription_id,
        time_entered__gte=F('license_plate__subscription__time_start'),
        time_left__lte=F('license_plate__subscription__time_end')
    ).select_related('license_plate', 'spot', 'lot')
    
    context = {
        'parking_history': parking_history
    }
    return render(request, 'subscription_detail.html', context)
def total_daily_parking_revenue(request, lot_id):
    total_revenue = BillingRecord.objects.filter(
        lot_id=lot_id,
        record__license_plate__subscription__lot_id=lot_id
    ).aggregate(total_revenue_daily_parking=Sum('amount'))['total_revenue_daily_parking']
    
    context = {
        'total_revenue_daily_parking': total_revenue
    }
    return render(request, 'parking_lot_detail.html', context)
def subscription_list(request):
    subscriptions = Subscription.objects.all().select_related(
        'license_plate', 'lot'
    )
    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'subscription_list.html', context)

def customer_detail(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    vehicles = Vehicle.objects.filter(customer=customer)
    subscriptions = Subscription.objects.filter(
        license_plate__in=vehicles.values_list('license_plate', flat=True)
    )
    billing_records = BillingRecord.objects.filter(customer=customer)
    
    print("Customer:", customer.first_name, customer.last_name)
    print("Vehicles:", list(vehicles.values()))
    print("Subscriptions:", list(subscriptions.values()))
    
    context = {
        'customer': customer,
        'vehicles': vehicles,
        'subscriptions': subscriptions,
        'billing_records': billing_records,
    }
    return render(request, 'customer_detail.html', context)

def create_parking_record(request, lot_id=None):
    if request.method == 'POST':
        form = ParkingRecordForm(request.POST)
        if form.is_valid():
            parking_record = form.save(commit=False)
            
            last_record = ParkingRecord.objects.order_by('record_id').last()
            parking_record.record_id = (last_record.record_id + 1) if last_record else 1
            
            parking_record.time_entered = timezone.now()
            
            spot = form.cleaned_data['spot']
            spot.status = 'occupied'
            spot.save()
            
            lot = form.cleaned_data['lot']
            if lot:
                lot.available_spots = lot.available_spots - 1
                lot.save()
            
            parking_record.save()
            messages.success(request, 'Vehicle parked successfully.')
            
            if lot_id:
                return redirect('parking_status_with_lot', lot_id=lot_id)
            return redirect('parking_status')
    else:
        initial_data = {}
        if lot_id:
            initial_data['lot'] = lot_id
        form = ParkingRecordForm(initial=initial_data)
    
    context = {
        'form': form,
        'lot_id': lot_id,
        'parking_lots': ParkingLot.objects.all(),
    }
    return render(request, 'parking_record_form.html', context)

def end_parking(request, record_id):
    parking_record = get_object_or_404(ParkingRecord, record_id=record_id)
    
    if request.method == 'POST':
        parking_record.time_left = timezone.now()
        parking_record.save()
        
        spot = parking_record.spot
        spot.status = 'available'
        spot.save()
        
        lot = parking_record.lot
        lot.available_spots = lot.available_spots + 1
        lot.save()
        
        messages.success(request, 'Parking ended successfully.')
        return redirect('parking_status', lot_id=parking_record.lot.lot_id if parking_record.lot else None)
    
    return render(request, 'parking_record_confirm_end.html', {
        'parking_record': parking_record
    })

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff_members': staff_members})

def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member created successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form, 'action': 'Create'})

def staff_update(request, staff_id):
    staff_member = get_object_or_404(Staff, staff_id=staff_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff member updated successfully.')
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff_member)
    return render(request, 'staff_form.html', {'form': form, 'action': 'Update'})

def staff_delete(request, staff_id):
    staff_member = get_object_or_404(Staff, staff_id=staff_id)
    if request.method == 'POST':
        staff_member.delete()
        messages.success(request, 'Staff member deleted successfully.')
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff_member': staff_member})