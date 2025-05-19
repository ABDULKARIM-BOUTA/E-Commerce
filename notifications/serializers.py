from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['pk', 'user', 'message', 'created_at']
        read_only_fields = ['pk', 'created_at']