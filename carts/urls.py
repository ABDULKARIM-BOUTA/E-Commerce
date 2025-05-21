from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('', views.CartListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.CartDetailView.as_view(), name='detail'),
    path('items/', views.CrtItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:id>/', views.CartItemDetailView.as_view(), name='item-detail')
]