from django.contrib import admin
from .models import PurchaseOrderModel


@admin.register(PurchaseOrderModel)
class PurchaseOrderAdmin(admin.ModelAdmin):

    list_display = ["po_number", "vendor", "quantity", "status"]
    