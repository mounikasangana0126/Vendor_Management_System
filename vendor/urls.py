
from django.urls import path,include
from .vendor_api import VendorAPI,VendorDetailAPI,VendorPerformanceDetailAPI


urlpatterns = [
    path('', VendorAPI.as_view(),name="VendorAPI"),
    path('<int:pk>/', VendorDetailAPI.as_view(),name="VendorDetailAPI"),
    path('<int:pk>/performance/', VendorPerformanceDetailAPI.as_view(),name="VendorPerformanceAPI")
]