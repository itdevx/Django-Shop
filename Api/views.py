from django.shortcuts import render
from rest_framework import generics
from Api.serializers import ProductSerializer
from Product.models import Product
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    

class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrive(self, request, pk):
        ...

    