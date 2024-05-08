from django.db import models
from vendor.models import VendorModel


class PerformanceMetricsModel(models.Model):
    vendor= models.ForeignKey(VendorModel,on_delete=models.CASCADE)
    date= models.DateTimeField()
    on_time_delivery_rate= models.FloatField()
    quality_rating_avg= models.FloatField()
    average_response_time= models.FloatField()
    fulfillment_rate= models.FloatField()