from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    # API Endpoints
    path('api/list-create', views.AdminOrderListCreateAPIView.as_view(), name='api-list-create'),
    path('api/user-list', views.UserOrderListCreateAPIView.as_view(), name='api-user-list'),
    path('api/<str:order_id>/detail', views.OrderUpdateDeleteAPIView.as_view(), name='api-detail'),

    # Template Views
    # path('', views.OrderListPageView.as_view(), name='page-list'),
    # path('<int:pk>/update-delete', views.OrderDetailPageView.as_view(), name='page-detail'),
#    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
]