from django.shortcuts import render
from rest_framework import generics
from Api.serializers import ProductSerializer
from Product.models import Product
from rest_framework import permissions


class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    