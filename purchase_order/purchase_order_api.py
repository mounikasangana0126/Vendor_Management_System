from rest_framework.views import APIView
from .serializer import PurchaseOrderSerializer
from .models import PurchaseOrderModel
from vendor.models import VendorModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.exceptions import NotFound
from vendor_performance_metrics.views import *
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone 

class PurchaseOrderAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        purchase_obj=PurchaseOrderModel.objects.all()
        serializer=PurchaseOrderSerializer(purchase_obj,many=True)
        return Response({'status':200,'message':"success",'payload':serializer.data})


    def post(self,request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            purchase_instance = serializer.save()
            vendor=VendorModel.objects.get(name=purchase_instance.vendor)
            calculate_vendor_metrics(request, vendor.id)
            return Response({'status': 200, 'message': "Purchase order created successfully",'payload':serializer.data})
        return Response({'status': 400, 'message': "Failed to create purchase order", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return PurchaseOrderModel.objects.get(pk=pk)
        except PurchaseOrderModel.DoesNotExist:
            raise NotFound("Purchase order does not exist")

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = PurchaseOrderSerializer(instance=snippet)
        return Response({'status': 200, 'message': "Purchase Order fetched successfully", 'payload': serializer.data})

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = PurchaseOrderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': "Purchase Order updated successfully", 'payload': serializer.data})
        return Response({'status': 400, 'message': "Failed to update purchase order", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        snippet = self.get_object(pk)
        if isinstance(snippet, Response): 
            return snippet  
        snippet.delete()
        return Response({'status': 200, 'message': "Purchase Order deleted successfully"})



class PurchaseAcknowledgeAPI(APIView):
    def post(self, request, pk):
        try:
            purchase_order = PurchaseOrderModel.objects.get(pk=pk)
            vendor=VendorModel.objects.get(id=pk)
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()
            calculate_vendor_metrics(request, vendor.id)
            return Response({'message': 'Purchase order acknowledged successfully'}, status=status.HTTP_200_OK)
        except PurchaseOrderModel.DoesNotExist:
            return Response({'error': 'Purchase order does not exist'}, status=status.HTTP_404_NOT_FOUND)
    