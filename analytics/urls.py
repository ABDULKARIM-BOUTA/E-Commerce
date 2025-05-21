from django.urls import path
from analytics import views

app_name = 'analytics'

urlpatterns = [
    path('', views.AnalyticsListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.AnalyticsDetailView.as_view(), name='detail')
]