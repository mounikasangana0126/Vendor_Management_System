# from django.urls import reverse
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from django.test import TestCase
# from rest_framework.test import APIClient

# from rest_framework.test import APITestCase

# from django.urls import reverse

# class VendorAPITests(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_vendor(self):
#         data = {
#             "name": "vendor",
#             "contact_details": "6282162245",
#             "address": "hyd",
#             "vendor_code": "123hyd"
#         }
#         url = reverse('VendorAPI')  # Assuming 'VendorAPI' is the name of your endpoint
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 401)
