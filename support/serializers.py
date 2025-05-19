from rest_framework import serializers
from support.models import Contact, FAQ

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['pk', 'name', 'message', 'email', 'created_at']
        read_only_fields = ['pk', 'created_at']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['pk', 'created_at', 'questions', 'answers']
        read_only_fields = ['pk', 'created_at']