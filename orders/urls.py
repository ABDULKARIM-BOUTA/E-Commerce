from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderListCreateView.as_view(), name='list-create'),
    path('<str:order_id>/', views.OrderDetailView.as_view(), name='detail'),

    path('items/', views.OrderItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:id>/', views.OrderItemDetailView.as_view(), name='item-detail'),

    path('coupons/', views.CouponListCreateView.as_view(), name='coupon-list-create'),
    path('coupons/<int:id>/', views.CouponDetailView.as_view(), name='coupon-detail'),

    path('subscription/', views.SubscriptionListCreateView.as_view(), name='sub-list-create'),
    path('subscription/<int:id>/', views.SubscriptionDetailView.as_view(), name='sub-detail'),

]