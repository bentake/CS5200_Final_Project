from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('parking-status/', views.parking_status, name='parking_status'),
    path('parking-status/<int:lot_id>/', views.parking_status, name='parking_status'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscriptions/<int:subscription_id>/', views.subscription_parking_history, name='subscription_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:customer_id>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),
    path('subscriptions/create/', views.subscription_create, name='subscription_create'),
    path('subscriptions/<int:subscription_id>/update/', views.subscription_update, name='subscription_update'),
    path('subscriptions/<int:subscription_id>/delete/', views.subscription_delete, name='subscription_delete'),
    path('parking-status/', views.parking_status, name='parking_status'),
    path('parking-status/<int:lot_id>/', views.parking_status, name='parking_status_with_lot'),
    path('parking-status/create/', views.create_parking_record, name='create_parking_record'),
    path('parking-status/<int:lot_id>/create/', views.create_parking_record, name='create_parking_record_lot'),
    path('parking-status/<int:record_id>/end/', views.end_parking, name='end_parking'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:staff_id>/update/', views.staff_update, name='staff_update'),
    path('staff/<int:staff_id>/delete/', views.staff_delete, name='staff_delete')
]