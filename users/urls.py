from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UserCreateView.as_view(), name='create'),
    path('<int:id>/', views.UserDetailView.as_view(), name='detail'),
]