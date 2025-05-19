from django.urls import path
from support import views

app_name = 'support'

urlpatterns = [
    path('', views.ContactListView.as_view(), name='list'),
    path('create/', views.ContactCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ContactDetailView.as_view(), name='detail'),

    path('faq/', views.FAQListView.as_view(), name='faq-list'),
    path('faq/create/', views.FAQCreateView.as_view(), name='faq-create'),
    path('faq/<int:pk>/', views.FAQDetailView.as_view(), name='faq-detail'),

]