from configuration.models import Configuration
from configuration.serializers import ConfigurationSerializer
from rest_framework import generics

class ConfigurationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    permission_classes = []

    # def get_object(self):
    #     # You likely have only one configuration instance
    #     return Configuration.objects.first()