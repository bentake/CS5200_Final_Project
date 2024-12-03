# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BillingRecord(models.Model):
    billing_id = models.IntegerField(db_column='Billing_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey('Customer', models.CASCADE, db_column='Customer_ID', blank=True, null=True)  # Added CASCADE
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    billing_date = models.DateField(db_column='Billing_date', blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lot = models.ForeignKey('ParkingLot', models.DO_NOTHING, db_column='Lot_ID', blank=True, null=True)  # Field name made lowercase.
    record = models.ForeignKey('ParkingRecord', models.DO_NOTHING, db_column='Record_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Billing_Record'


class Customer(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', primary_key=True)
    first_name = models.CharField(db_column='First_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=30, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=6, blank=True, null=True) 
    def save(self, *args, **kwargs):
        if not self.customer_id:  # If no ID is provided, assign it manually
            last_customer = Customer.objects.all().order_by('customer_id').last()
            if last_customer:
                self.customer_id = last_customer.customer_id + 1
            else:
                self.customer_id = 1  # Start from 1 if no customer exists yet
        super().save(*args, **kwargs)
     # Field name made lowercase.
 
    class Meta:
        managed = False
        db_table = 'Customer'


class ParkingGate(models.Model):
    gate_id = models.IntegerField(db_column='Gate_ID', primary_key=True)  # Field name made lowercase.
    is_operational = models.IntegerField(db_column='Is_operational', blank=True, null=True)  # Field name made lowercase.
    installed_in = models.ForeignKey('ParkingLot', models.DO_NOTHING, db_column='Installed_in', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parking_Gate'


class ParkingLot(models.Model):
    lot_id = models.IntegerField(db_column='Lot_ID', primary_key=True)  # Field name made lowercase.
    number_of_spots = models.IntegerField(db_column='Number_of_spots', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=30, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=6, blank=True, null=True)  # Field name made lowercase.
    available_spots = models.IntegerField(db_column='Available_spots', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parking_Lot'


class ParkingRecord(models.Model):
    record_id = models.IntegerField(db_column='Record_ID', primary_key=True)  # Field name made lowercase.
    license_plate = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='License_plate', blank=True, null=True)  # Field name made lowercase.
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='Spot_ID', blank=True, null=True)  # Field name made lowercase.
    time_entered = models.DateTimeField(db_column='Time_entered', blank=True, null=True)  # Field name made lowercase.
    time_left = models.DateTimeField(db_column='Time_left', blank=True, null=True)  # Field name made lowercase.
    lot = models.ForeignKey(ParkingLot, models.DO_NOTHING, db_column='Lot_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parking_Record'


class ParkingZone(models.Model):
    zone_id = models.IntegerField(db_column='Zone_ID', primary_key=True)  # Field name made lowercase.
    zone_name = models.CharField(db_column='Zone_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zone_type = models.CharField(db_column='Zone_type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    zone_capacity = models.IntegerField(db_column='Zone_capacity', blank=True, null=True)  # Field name made lowercase.
    lot = models.ForeignKey(ParkingLot, models.DO_NOTHING, db_column='Lot_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parking_Zone'


class Spot(models.Model):
    spot_id = models.IntegerField(db_column='Spot_ID', primary_key=True)
    lot = models.ForeignKey(ParkingLot, models.DO_NOTHING, db_column='Lot_ID', blank=True, null=True)
    status = models.CharField(db_column='Spot_status', max_length=10, blank=True, null=True)  # Updated this line

    class Meta:
        managed = False
        db_table = 'Spot'


class Staff(models.Model):
    staff_id = models.IntegerField(db_column='Staff_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shift_start = models.TimeField(db_column='Shift_start', blank=True, null=True)  # Field name made lowercase.
    shift_end = models.TimeField(db_column='Shift_end', blank=True, null=True)  # Field name made lowercase.
    lot = models.ForeignKey(ParkingLot, models.DO_NOTHING, db_column='Lot_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class Subscription(models.Model):
    subscription_id = models.IntegerField(db_column='Subscription_ID', primary_key=True)  # Field name made lowercase.
    lot = models.ForeignKey(ParkingLot, models.DO_NOTHING, db_column='Lot_ID', blank=True, null=True)  # Field name made lowercase.
    license_plate = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='License_plate', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    time_start = models.DateTimeField(db_column='Time_start', blank=True, null=True)  # Field name made lowercase.
    time_end = models.DateTimeField(db_column='Time_end', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subscription'


class Vehicle(models.Model):
    license_plate = models.CharField(db_column='License_plate', primary_key=True, max_length=10)
    make = models.CharField(db_column='Make', max_length=15, blank=True, null=True)
    model = models.CharField(db_column='Model', max_length=15, blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer_ID', related_name='vehicles', blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=5, blank=True, null=True)
    number_of_doors = models.IntegerField(db_column='Number_of_doors', blank=True, null=True)
    fuel_type = models.CharField(db_column='Fuel_type', max_length=10, blank=True, null=True)
    cargo_capacity = models.IntegerField(db_column='Cargo_capacity', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vehicle'

