from rest_framework import serializers
from analytics.models import Analytics
from products.serializers import ProductSerializer

class AnalyticsSerializer(serializers.ModelSerializer):
    popular_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Analytics
        fields = ['id', 'sales', 'traffic', 'popular_products', 'created_at']
        read_only_fields = ['id', 'created_at']