from rest_framework import serializers
from orders.models import Order, OrderItem, Coupon, Subscription
from django.contrib.auth import get_user_model
from django.db import transaction
from users.serializers import UserSerializer
from products.serializers import ProductSerializer

User = get_user_model()

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', decimal_places=2, max_digits=10)

    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_price', 'quantity', 'item_total_price']
        read_only_fields = ['item_total_price']

class OrderSerializer(serializers.ModelSerializer):
   # items = OrderItemSerializer(many=True, read_only=True)     # nested serializer to list the details of order items
   # user = UserSerializer(read_only=True)
   # total_amount = serializers.SerializerMethodField()
    #
    # def get_total_amount(self, obj):
    #     # to calculate all the order items prices
    #     order_items = obj.items.all()
    #     total_amount = 0
    #
    #     for order_item in order_items:
    #         total_amount += order_item.item_total_price
    #     return total_amount

    user = UserSerializer(read_only=True)
    products = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'user', 'products', 'created_at', 'shipping_address'] # 'total_amount' 'status' , 'order_items' , 'payment_method',
        read_only_fields = ['order_id', 'created_at'] # "total_amount'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['pk', 'code', 'discount_value', 'valid_from', 'valid_to']
        read_only_fields = ['pk']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['pk', 'email', 'created_at']
        read_only_fields = ['pk', 'created_at']


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ['product', 'quantity']

    items = OrderItemCreateSerializer(many=True, required=False)     # nested serializer to list the details of order items
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'user','address','payment_method', 'items']

    def create(self, validated_data):
        # create order and each order item because they are related
        order_items_list = validated_data.pop('items')

        with transaction.atomic():
            order = Order.objects.create(**validated_data)
            for order_item in order_items_list:
                OrderItem.objects.create(order=order, **order_item)

        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('items', [])

        with transaction.atomic():
            # update the Order fields
            instance = super().update(instance, validated_data)

            # keep track of existing items
            existing_items = {item.product_id: item for item in instance.items.all()}

            for item_data in order_items_data:
                product = item_data['product']
                quantity = item_data['quantity']

                if product.id in existing_items:
                    # update the existing item
                    order_item = existing_items[product.id]
                    order_item.quantity = quantity
                    order_item.save()
                else:
                    # create a new item
                    OrderItem.objects.create(order=instance, **item_data)
        return instance