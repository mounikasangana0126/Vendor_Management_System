from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from vendor.models import VendorModel  

class VendorAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_vendor(self):
        data = {
            "name": "vendor",
            "contact_details": "6282162245",
            "address": "hyd",
            "vendor_code": "123hyd"
        }
        url = reverse('VendorAPI') 
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_vendors(self):
        url = reverse('VendorAPI')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
      

    def test_get_vendor_detail(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        url = reverse('VendorDetailAPI', kwargs={'pk': vendor.id})  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
       

    def test_update_vendor(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        updated_data = {
            "name": "Updated Vendor",
            "contact_details": "0987654321",
            "address": "Updated Address",
            "vendor_code": "456"
        }
        url = reverse('VendorDetailAPI', kwargs={'pk': vendor.id}) 
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    def test_delete_vendor(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        url = reverse('VendorDetailAPI', kwargs={'pk': vendor.id})  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
