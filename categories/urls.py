from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    # api urls
    path('api/list-create/', views.CategoryListCreateAPIView.as_view(), name='api-list-create'),
    path('api/<int:pk>/detail/', views.CategoryUpdateDeleteAPIView.as_view(), name='api-detail'),

    # templates urls
    path('list-create/', views.CategoryListCreatePageView.as_view(), name='page-list-create'),
    path('<int:pk>/detail/', views.CategoryUpdateDeletePageView.as_view(), name='page-detail'),
]