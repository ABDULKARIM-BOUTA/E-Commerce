from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import Order
from django.views.generic import TemplateView

# api views
class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = []

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = []

    def get_queryset(self):
        return Order.objects.all()

    def perform_update(self, serializer):
        # to show total amount after calculating all items quantity and price

        instance = serializer.save()
        instance.total_amount = 0

        if 'items' in serializer.validated_data:
            for item in instance.items.all():
                instance.total_amount = sum(item.quantity * item.price)
            instance.save()

# Template views
class OrderListPageView(TemplateView):
    template_name = 'orders/list.html'

class OrderDetailPageView(TemplateView):
    template_name = 'orders/detail.html'
