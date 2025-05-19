from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from vendors.serializers import VendorSerializer
from vendors.models import Vendor

class VendorListCreateView(ListCreateAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    permission_classes = []

class VendorDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    permission_classes = []