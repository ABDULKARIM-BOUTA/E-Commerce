from rest_framework import serializers
from users.models import User

# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']