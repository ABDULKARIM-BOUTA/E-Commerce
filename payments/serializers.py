from rest_framework import serializers
from payments.models import Payment, Refund
from orders.serializers import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['pk', 'order', 'method', 'amount', 'transaction_id', 'created_at']
        read_only_fields = ['created_at', 'pk']

class RefundSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Refund
        fields = ['pk', 'order', 'reason', 'amount', 'created_at', 'processed_at', 'status']
        read_only_fields = ['pk', 'created_at']