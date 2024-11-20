from rest_framework import serializers
from Product.models import Product, Category
from Cart.models import Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    category = CategorySerializer()


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        