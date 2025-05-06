from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    # api urls
    path('api/list/', views.ProductListAPIView.as_view(), name='api-list'),
    path('api/create/', views.ProductCreateAPIView.as_view(), name='api-create'),
    path('api/<int:pk>/detail/', views.ProductDetailAPIView.as_view(), name='api-detail'),
    path('api/<int:pk>/update-delete/', views.ProductUpdateDeleteAPIView.as_view(), name='api-update-delete'),

    # templates urls
    path('list/', views.ProductListPageView.as_view(), name='page-list'),
    path('create/', views.ProductCreatePageView.as_view(), name='page-create'),
    path('<int:pk>/detail/', views.ProductDetailPageView.as_view(), name='page-detail'),
    path('<int:pk>/update-delete/', views.ProductUpdateDeletePageView.as_view(), name='page-update-delete'),
]