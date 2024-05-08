from rest_framework.views import APIView
from .serializer import VendorSerializer,VendorPerformanceSerializer
from .models import VendorModel
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from vendor_performance_metrics.views import *

class VendorAPI(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request)
        vendor_obj=VendorModel.objects.all()
        serializer=VendorSerializer(vendor_obj,many=True)
        return Response({'status':200,'message':"success",'payload':serializer.data})

    def post(self,request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            vendor_instance = serializer.save()
            return Response({'status': 200, 'message': "Vendor created successfully",'payload':serializer.data})
        return Response({'status': 400, 'message': "Failed to create vendor", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VendorDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return VendorModel.objects.get(pk=pk)
        except VendorModel.DoesNotExist:
            raise NotFound("Vendor does not exist")

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = VendorSerializer(instance=snippet)
        return Response({'status': 200, 'message': "Vendor fetched successfully", 'payload': serializer.data})

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = VendorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': "Vendor updated successfully", 'payload': serializer.data})
        return Response({'status': 400, 'message': "Failed to update Vendor", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        snippet = self.get_object(pk)
        if isinstance(snippet, Response):
            return snippet  
        snippet.delete()
        return Response({'status': 200, 'message': "Vendor deleted successfully"})


class VendorPerformanceDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return VendorModel.objects.get(pk=pk)
        except VendorModel.DoesNotExist:
            raise NotFound("Vendor does not exist")

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = VendorPerformanceSerializer(instance=snippet)
        return Response({'status': 200, 'message': "Purchase Order fetched successfully", 'payload': serializer.data})