from rest_framework import serializers
from shipping.models import Shipping

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ['pk', 'name', 'price', 'description', 'rate', 'is_active', 'estimate_delivery_time']
        read_only_fields = ['pk']