from payments.serializers import PaymentSerializer, RefundSerializer
from payments.models import Payment, Refund
from rest_framework import generics

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = []

class PaymentDetailView(generics.RetrieveAPIView):
    """using retrieve only to prevent modifying payment records"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = []

class RefundListCreateView(generics.ListCreateAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    permission_classes = []

class RefundDetailView(generics.RetrieveUpdateAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    permission_classes = []