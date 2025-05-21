from rest_framework import serializers
from vendors.models import Vendor
from users.serializers import UserSerializer

class VendorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'user', 'store_description', 'store_name', 'bank_details', 'store_logo',
                  'created_at', 'contact_details', 'shipping_policy', 'refund_policy']
        read_only_fields = [' created_at', 'id']