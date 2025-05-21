from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    # api urls
    path('', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='detail'),

    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:id>', views.ReviewDetailView.as_view(), name='review-detail'),

    # # templates urls
    # path('list/', views.ProductListPageView.as_view(), name='page-list'),
    # path('create/', views.ProductCreatePageView.as_view(), name='page-create'),
    # path('<int:pk>/detail/', views.ProductDetailUpdateDeletePageView.as_view(), name='page-detail'),
]