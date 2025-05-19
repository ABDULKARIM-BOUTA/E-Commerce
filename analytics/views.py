from rest_framework import generics
from analytics.models import Analytics
from analytics.serializers import AnalyticsSerializer

class AnalyticsListCreateView(generics.ListCreateAPIView):
    serializer_class = AnalyticsSerializer
    queryset = Analytics.objects.all()
    permission_classes = []

class AnalyticsDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = AnalyticsSerializer
    queryset = Analytics.objects.all()
    permission_classes = []