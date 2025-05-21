from rest_framework import serializers
from payments.models import Payment, Refund
from orders.serializers import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'method', 'amount', 'transaction_id', 'created_at']
        read_only_fields = ['created_at', 'id']

class RefundSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Refund
        fields = ['id', 'order', 'reason', 'amount', 'created_at', 'processed_at', 'status']
        read_only_fields = ['id', 'created_at']