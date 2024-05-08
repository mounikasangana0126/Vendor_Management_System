from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from purchase_order.models import PurchaseOrderModel  
from vendor.models import VendorModel  

class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_purchase_order(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        data = {
            "vendor": vendor.id,
            "po_number": "PO123",
            "order_date": "2024-05-10T12:00:00Z",
            "delivery_date": "2024-05-20T12:00:00Z",
            "items": ["Item 1", "Item 2"],
            "quantity": 10,
            "status": "pending",
            "issue_date": "2024-05-10T12:00:00Z" 
        }
        url = reverse('purchaseapi')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_purchase_orders(self):
        url = reverse('purchaseapi') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_purchase_order_detail(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        issue_date = timezone.now() 
        purchase_order = PurchaseOrderModel.objects.create(vendor=vendor, po_number="PO123", order_date="2024-05-10T12:00:00Z", delivery_date="2024-05-20T12:00:00Z", items=["Item 1", "Item 2"], quantity=10, status="pending", issue_date=issue_date)
        url = reverse('purchasedetailapi', kwargs={'pk': purchase_order.id})
        response = self.client.get(url)  
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    def test_update_purchase_order(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        issue_date = timezone.now()  
        purchase_order = PurchaseOrderModel.objects.create(vendor=vendor, po_number="PO123", order_date="2024-05-10T12:00:00Z", delivery_date="2024-05-20T12:00:00Z", items=["Item 1", "Item 2"], quantity=10, status="pending", issue_date=issue_date)
        updated_data = {
            "vendor": vendor.id,
            "po_number": "PO456",
            "order_date": "2024-05-15T12:00:00Z",
            "delivery_date": "2024-05-25T12:00:00Z",
            "items": ["Item 1", "Item 2", "Item 3"],
            "quantity": 20,
            "status": "approved",
            "issue_date": "2024-05-15T12:00:00Z"  
        }
        url = reverse('purchasedetailapi', kwargs={'pk': purchase_order.id})  
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
     

    def test_delete_purchase_order(self):
        vendor = VendorModel.objects.create(name="Test Vendor", contact_details="1234567890", address="Test Address", vendor_code="TEST123")
        issue_date = timezone.now()  
        purchase_order = PurchaseOrderModel.objects.create(vendor=vendor, po_number="PO123", order_date="2024-05-10T12:00:00Z", delivery_date="2024-05-20T12:00:00Z", items=["Item 1", "Item 2"], quantity=10, status="pending", issue_date=issue_date)
        url = reverse('purchasedetailapi', kwargs={'pk': purchase_order.id}) 
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
       
