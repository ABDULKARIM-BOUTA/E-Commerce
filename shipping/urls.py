from django.urls import path
from shipping import views

app_name = 'shipping'

urlpatterns = [
    path('', views.ShippingListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.ShippingDetailView.as_view(), name='detail'),
]