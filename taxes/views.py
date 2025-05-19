from taxes.models import Tax
from taxes.serializers import TaxSerializer
from rest_framework import generics

class TaxListCreateView(generics.ListCreateAPIView):
    serializer_class = TaxSerializer
    queryset = Tax.objects.all()
    permission_classes = []

class TaxDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaxSerializer
    queryset = Tax.objects.all()
    permission_classes = []

