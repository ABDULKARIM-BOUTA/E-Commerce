from rest_framework import serializers
from blogs.models import Blog
from users.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at', 'slug']
        read_only_fields = ['id', 'created_at', 'updated_at', 'slug']
