from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    # API Endpoints
    path('api/list-create', views.OrderListCreateAPIView.as_view(), name='api-list-create'),
    path('api/<int:pk>/update-delete', views.OrderUpdateDeleteAPIView.as_view(), name='api-update-delete'),

    # Template Views
    path('', views.OrderListPageView.as_view(), name='page-list'),
    path('<int:pk>/update-delete', views.OrderDetailPageView.as_view(), name='page-update-delete'),
#    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
]