from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    # api urls
    path('api/list/', views.ProductListAPIView.as_view(), name='api-list'),
    path('api/create/', views.ProductCreateAPIView.as_view(), name='api-create'),
    path('api/<int:pk>/detail/', views.ProductDetailUpdateDeleteAPIView.as_view(), name='api-detail'),

    # templates urls
    path('list/', views.ProductListPageView.as_view(), name='page-list'),
    path('create/', views.ProductCreatePageView.as_view(), name='page-create'),
    path('<int:pk>/update-delete/', views.ProductDetailUpdateDeletePageView.as_view(), name='page-update-delete'),
]