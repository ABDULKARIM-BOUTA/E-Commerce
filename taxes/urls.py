from django.urls import path
from taxes import views

app_name = 'taxes'

urlpatterns = [
    path('', views.TaxListCreateView.as_view(), name='list-create'),
    path('<int:id>/', views.TaxDetailView.as_view(), name='detail'),
]