from rest_framework import serializers
from .models import VendorModel

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorModel
        fields=[
          "id",
          "name",
          "contact_details",
          "address",
          "vendor_code",
          "on_time_delivery_rate",
          "quality_rating_avg",
          "average_response_time",
          "fulfillment_rate",
        ]
class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorModel
        fields=[
          "id",
          "on_time_delivery_rate",
          "quality_rating_avg",
          "average_response_time",
          "fulfillment_rate",
        ]