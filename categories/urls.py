from django.urls import path
from categories import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryListCreateView.as_view(), name='list-create'),
    path('detail/<int:id>/', views.CategoryDetailView.as_view(), name='detail'),
]
