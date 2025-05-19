from django.urls import path
from vendors import views

app_name = 'vendors'

urlpatterns = [
    path('', views.VendorListCreateView.as_view(), name='list-create'),
    path('<int:pk>/', views.VendorDetailView.as_view(), name='detail'),
]