from django.urls import path
from wishlists import views

app_name = 'wishlists'

urlpatterns = [
    path('', views.WishlistListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.WishlistDetailView.as_view(), name='detail'),
]