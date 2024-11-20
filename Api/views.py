from django.shortcuts import render
from rest_framework import generics
from Api.serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemSerilizer
from Product.models import Product, Category
from Cart.models import Cart, CartItem
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin
from django.utils.text import slugify



class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
        

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'description', 'price']
    pagination_class = PageNumberPagination
    


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CartViewSet(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerilizer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'slug'
    queryset = CartItem.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return CartItem.objects.filter(cart__user=user)
    
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user, slug=slugify(self.request.user))
