from rest_framework import serializers
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent_category']
        read_only_fields = ['slug']