from django.db import models
from vendor.models import VendorModel


class PurchaseOrderModel(models.Model):
    po_number= models.CharField(max_length=50,unique=True)
    vendor= models.ForeignKey(VendorModel,on_delete=models.CASCADE)
    order_date= models.DateTimeField()
    delivery_date= models.DateTimeField()
    items= models.JSONField()
    quantity= models.IntegerField()
    status= models.CharField(max_length=50)
    quality_rating= models.FloatField(null=True,blank=True)
    issue_date= models.DateTimeField()
    acknowledgment_date= models.DateTimeField(null=True,blank=True)


   