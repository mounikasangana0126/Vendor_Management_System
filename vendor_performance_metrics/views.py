from django.shortcuts import render
from purchase_order.models import PurchaseOrderModel
from .models import PerformanceMetricsModel
from django.utils import timezone
from vendor.models import VendorModel
from .models import PerformanceMetricsModel
from django.http import HttpResponse
from django.db.models import F,Avg



def calculate_on_time_delivery(vendor):
    completed_pos = PurchaseOrderModel.objects.filter(vendor=vendor, status="completed").count()
    if completed_pos == 0:
        return 0 
    on_time_deliveries = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed', delivery_date__lte=F('acknowledgment_date')).count()
    return (on_time_deliveries / completed_pos) * 100

def calculate_quality_rating_average(vendor):
    avg = PurchaseOrderModel.objects.filter(vendor=vendor, status="completed").aggregate(avg_quality_rating=Avg("quality_rating"))['avg_quality_rating']
    return avg or 0 

def calculate_average_response_time(vendor):
    value = PurchaseOrderModel.objects.filter(vendor=vendor)
    response_time=value.annotate(sub=F("acknowledgment_date") - F("issue_date")).aggregate(avg_response_time=Avg("sub"))['avg_response_time']
    if response_time:
        response_time_seconds = response_time.total_seconds()
        return response_time_seconds
        print(response_time_seconds)
    return 0

def calculate_fulfilment_rate(vendor):
    total_pos = PurchaseOrderModel.objects.filter(vendor=vendor).count()
    if total_pos == 0:
        return 0  
    fulfilled_pos = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed').count()
    return (fulfilled_pos / total_pos) * 100

def calculate_vendor_metrics(request, vendor_id):
    vendor = VendorModel.objects.get(id=vendor_id)
    on_time_delivery_rate = calculate_on_time_delivery(vendor)
    quality_rating_avg = calculate_quality_rating_average(vendor)
    average_response_time = calculate_average_response_time(vendor)
    fulfilment_rate = calculate_fulfilment_rate(vendor)

    
    # Update VendorModel instance with calculated metrics
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.average_response_time = average_response_time
    vendor.fulfillment_rate = fulfilment_rate
    vendor.save() 

    # Create Performance Metrics instance with calculated metrics

    PerformanceMetricsModel.objects.create(
        vendor=vendor,
        date=timezone.now(),
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        average_response_time=average_response_time,
        fulfillment_rate=fulfilment_rate
    )