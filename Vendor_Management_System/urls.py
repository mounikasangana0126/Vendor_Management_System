
from django.contrib import admin
from django.urls import path,include
from .vms_api import ObtainTokenView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendors/', include('vendor.urls')),
    path('purchase_orders/', include('purchase_order.urls')),
    path('auth/', ObtainTokenView.as_view(),name="vmsApi")
]
