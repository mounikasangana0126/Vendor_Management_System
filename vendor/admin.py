from django.contrib import admin
from .models import VendorModel




@admin.register(VendorModel)
class VendorAdmin(admin.ModelAdmin):
    list_display=["name","vendor_code","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate",]