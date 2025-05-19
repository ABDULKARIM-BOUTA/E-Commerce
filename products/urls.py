from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    # api urls
    path('api/list/', views.ProductListView.as_view(), name='api-list'),
    path('api/create/', views.ProductCreateView.as_view(), name='api-create'),
    path('api/<int:pk>/detail/', views.ProductDetailView.as_view(), name='api-detail'),

    # templates urls
    path('list/', views.ProductListPageView.as_view(), name='page-list'),
    path('create/', views.ProductCreatePageView.as_view(), name='page-create'),
    path('<int:pk>/detail/', views.ProductDetailUpdateDeletePageView.as_view(), name='page-detail'),
]