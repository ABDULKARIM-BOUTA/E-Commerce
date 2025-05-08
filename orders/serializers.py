from rest_framework import serializers
from orders.models import Order, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', decimal_places=2, max_digits=10)

    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_price', 'quantity', 'item_total_price']
        read_only_fields = ['item_total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)     # nested serializer to list the details of order items
    user = serializers.StringRelatedField(read_only=True)
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        # to calculate all the order items prices
        order_items = obj.items.all()
        total_amount = 0

        for order_item in order_items:
            total_amount += order_item.item_total_price
        return total_amount

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'user', 'created_at', 'address', 'payment_method', 'total_amount', 'items']
        read_only_fields = ['order_id', 'created_at', 'total_amount']


class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ['product', 'quantity']

    items = OrderItemCreateSerializer(many=True)     # nested serializer to list the details of order items
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'user','address','payment_method', 'items']

    def create(self, validated_data):
        # create order and each order item because they are related
        order_items_list = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for order_item in order_items_list:
            OrderItem.objects.create(order=order, **order_item)
        return order