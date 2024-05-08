from django.db import models

# Create your models here.

class VendorModel(models.Model):
    name= models.CharField(max_length=100)
    contact_details= models.TextField()
    address= models.TextField()
    vendor_code=models.CharField(max_length=50,unique=True)
    on_time_delivery_rate= models.FloatField(default=0)
    quality_rating_avg= models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfillment_rate= models.FloatField(default=0)

    def __str__(self):
        """Return a string representation of the object."""
        return str(self.name)

    class Meta:
        """Class Meta."""

        ordering = ["name"]