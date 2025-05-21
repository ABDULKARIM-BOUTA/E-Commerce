from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import TemplateView
from rest_framework.permissions import IsAdminUser

class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [] #IsAdminUser

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [] #IsAdminUser

# class CategoryListCreatePageView(TemplateView):
#     template_name = 'categories/list-create'
#     permission_classes = [IsAdminUser]
#
# class CategoryUpdateDeletePageView(TemplateView):
#     template_name = 'categories/update-delete.html'
#     permission_classes = [IsAdminUser]