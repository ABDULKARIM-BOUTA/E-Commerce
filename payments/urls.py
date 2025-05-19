from django.urls import path
from payments import views

app_name = 'payments'

urlpatterns = [
    path('', views.PaymentListCreateView.as_view(), name='list-create'),
    path('<int:pk>/', views.PaymentDetailView.as_view(), name='detail'),

    path('refund/', views.RefundListCreateView.as_view(), name='list-create'),
    path('refund/<int:pk>/', views.RefundDetailView.as_view(), name='detail'),
]