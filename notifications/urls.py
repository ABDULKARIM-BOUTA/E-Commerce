from django.urls import path
from notifications import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.NotificationDetailView.as_view(), name='detail'),
]