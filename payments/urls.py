from django.urls import path
from payments import views

app_name = 'payments'

urlpatterns = [
    path('', views.PaymentListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.PaymentDetailView.as_view(), name='detail'),

    path('refund/', views.RefundListCreateView.as_view(), name='list-create'),
    path('refund/<int:id>/', views.RefundDetailView.as_view(), name='detail'),
]