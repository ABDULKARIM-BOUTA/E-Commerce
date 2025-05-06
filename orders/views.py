from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.generic import TemplateView

# api views
class AdminOrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Order.objects.prefetch_related('items__product').all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserOrderListCreateAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.prefetch_related('items__product').filter(user=user)

class OrderUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'order_id'

    def get_queryset(self):
        user = self.request.user
        return Order.objects.prefetch_related('items__product').filter(user=user)

# Template views
# class OrderListPageView(TemplateView):
#     template_name = 'orders/list.html'
#
# class OrderDetailPageView(TemplateView):
#     template_name = 'orders/detail.html'
