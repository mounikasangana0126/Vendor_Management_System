from django.contrib import admin
from .models import PerformanceMetricsModel

# Register your models here.

@admin.register(PerformanceMetricsModel)
class PerformanceMetricsAdmin(admin.ModelAdmin):
    list_display=["vendor","date","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate"]