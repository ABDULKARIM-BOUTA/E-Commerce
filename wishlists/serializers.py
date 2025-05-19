from rest_framework import serializers
from wishlists.models import Wishlist
from products.serializers import ProductSerializer
from users.serializers import UserSerializer

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['pk', 'user','product', 'created_at']
        read_only_fields = ['pk']