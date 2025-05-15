from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from orders.serializers import OrderSerializer, OrderCreateUpdateSerializer
from orders.models import Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from orders.tasks import send_order_confirmation_email

# api views
class AdminOrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        # if it is a create method, it changes the serializer
        method = self.request.method
        if method  == 'POST':
            self.serializer_class = OrderCreateUpdateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return Order.objects.prefetch_related('items__product').all()

    @method_decorator(cache_page(60 * 10, key_prefix='admin_orders_list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserOrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # cashing with vary on headers so a user only gets their order list  
    @method_decorator(vary_on_headers("Autherization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        method = self.request.method
        if method == 'POST':
            return OrderCreateUpdateSerializer
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        user = self.request.user
        order = serializer.save(user=user)
        send_order_confirmation_email.delay(order.order_id, user.email)

    def get_queryset(self):
        user = self.request.user
        return Order.objects.prefetch_related('items__product').filter(user=user)

class OrderUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'order_id'

    def perform_update(self, serializer):
        user = self.request.user
        order = serializer.save(user=user)
        send_order_confirmation_email.delay(str(order.order_id), str(user.email))

    def get_queryset(self):
        user = self.request.user
        return Order.objects.prefetch_related('items__product').filter(user=user)


# Template views

# class OrderListPageView(TemplateView):
#     template_name = 'orders/list.html'
#
# class OrderDetailPageView(TemplateView):
#     template_name = 'orders/detail.html'
