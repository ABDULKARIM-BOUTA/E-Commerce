from rest_framework import serializers
from carts.models import Cart, CartItem
from products.serializers import ProductSerializer
from users.serializers import UserSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', decimal_places=2, max_digits=10)

    class Meta:
        model = CartItem
        fields = ['product_name', 'product_price', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = ProductSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'created_at', 'updated_at', 'session_id', 'items']
        read_only_fields = ['user', 'created_at', 'updated_at']