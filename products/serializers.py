from products.models import Product
from rest_framework import serializers
from categories.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name', required=True, allow_null=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'price', 'stock_quantity', 'description',
                  'created_at', 'updated_at', 'category', 'manufacturer', 'image']

        read_only_fields = ['pk', 'created_at', 'updated_at']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price Must be higher than 0')
        return value