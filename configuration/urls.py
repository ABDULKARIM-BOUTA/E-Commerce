from django.urls import path
from configuration import views

app_name = 'configuration'

urlpatterns = [
    path('<int:id>/', views.ConfigurationDetailView.as_view(), name='detail'),
]