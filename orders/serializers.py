from rest_framework import serializers
from orders.models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'total_price']
        read_only_fields = ['total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)     # nested serializer to show the order items in the order

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'user', 'created_at','address',
                  'total_amount', 'payment_method', 'items']