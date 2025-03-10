from rest_framework import serializers
from products.models import Product, Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)

class CartSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cart
        fields = '__all__'
