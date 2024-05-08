from rest_framework import serializers
from .models import PurchaseOrderModel

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrderModel
        fields=[
          "id",
          "po_number",
          "vendor",
          "order_date",
          "delivery_date",
          "items",
          "quantity",
          "status",
          "quality_rating",
          "issue_date",
          "acknowledgment_date"
        ]
        