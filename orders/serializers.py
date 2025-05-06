from rest_framework import serializers
from orders.models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    #product = ProductSerializer()    # nested serializer to list the details of a product
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', decimal_places=2, max_digits=10)

    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_price', 'quantity', 'total_price']
        read_only_fields = ['total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)     # nested serializer to list the details of order items
    total_amount =serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        # to calculate all the order items prices
        order_items = obj.items.all()
        total_amount = 0

        for order_item in order_items:
            total_amount += order_item.total_price

        return total_amount

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'user', 'created_at','address',
                  'total_amount', 'payment_method', 'items']

        read_only_fields = ['order_id', 'user', 'created_at', 'total_amount']