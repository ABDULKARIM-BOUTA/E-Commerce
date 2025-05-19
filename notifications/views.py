from rest_framework import generics
from notifications.serializers import NotificationSerializer
from notifications.models import Notification

class NotificationListCreateView(generics.ListCreateAPIView):
    permission_classes = []
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()