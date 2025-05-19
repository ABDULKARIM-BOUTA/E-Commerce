from rest_framework import generics
from orders.serializers import OrderSerializer, OrderCreateUpdateSerializer, OrderItemSerializer, CouponSerializer, SubscriptionSerializer
from orders.models import Order, OrderItem, Coupon, Subscription
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from orders.tasks import send_order_confirmation_email

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = []

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

class OrderDetailView(generics.RetrieveAPIView):
    """retrieve only so after making an order it cant be updated or deleted"""
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

class OrderItemListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = []

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = []

class CouponListCreateView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = []

class CouponDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = []

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = []

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = []

# api views
# class AdminOrderListCreateAPIView(ListCreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAdminUser]
#
#     def get_serializer_class(self):
#         # if it is a create method, it changes the serializer
#         method = self.request.method
#         if method  == 'POST':
#             self.serializer_class = OrderCreateUpdateSerializer
#         return super().get_serializer_class()
#
#     def get_queryset(self):
#         return Order.objects.prefetch_related('items__product').all()
#
#     @method_decorator(cache_page(60 * 10, key_prefix='admin_orders_list'))
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# Template views

# class OrderListPageView(TemplateView):
#     template_name = 'orders/list.html'
#
# class OrderDetailPageView(TemplateView):
#     template_name = 'orders/detail.html'
