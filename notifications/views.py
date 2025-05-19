from rest_framework import generics
from notifications.serializers import NotificationSerializer
from notifications.models import Notification

class NotificationListCreate(generics.ListCreateAPIView):
    permission_classes = []
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()