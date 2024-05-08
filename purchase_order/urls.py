
from django.urls import path,include
from .purchase_order_api import PurchaseOrderAPI,PurchaseOrderDetailAPI, PurchaseAcknowledgeAPI


urlpatterns = [
    path('', PurchaseOrderAPI.as_view(),name="purchaseapi"),
    path('<int:pk>/', PurchaseOrderDetailAPI.as_view(),name="purchasedetailapi"),
    path('<int:pk>/acknowledge/', PurchaseAcknowledgeAPI.as_view(),name="purchaseacknowledgeapi")
]