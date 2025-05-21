from products.models import Product, Review
from rest_framework import serializers
from categories.serializers import CategorySerializer
from vendors.serializers import VendorSerializer
from users.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock_quantity', 'description', 'reviews',
                  'created_at', 'updated_at', 'category', 'vendor', 'image', 'slug']

        read_only_fields = ['id', 'created_at', 'updated_at', 'slug']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price Must be higher than 0')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


