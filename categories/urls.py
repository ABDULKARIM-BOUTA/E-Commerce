from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    # api urls
    path('api/list-create/', views.CategoryListCreateAPIView.as_view(), name='api-list-create'),
    path('api/<int:pk>/update-delete/', views.CategoryUpdateDeleteAPIView.as_view(), name='api-update-delete'),

    # templates urls
    path('list-create/', views.CategoryListCreatePageView.as_view(), name='page-list-create'),
    path('<int:pk>/update-delete/', views.CategoryUpdateDeletePageView.as_view(), name='page-update-delete'),
]