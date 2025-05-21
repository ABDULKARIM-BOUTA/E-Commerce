from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.BlogDetailView.as_view(), name='detail'),
]