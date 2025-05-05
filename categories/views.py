from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import TemplateView

class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryListCreatePageView(TemplateView):
    template_name = 'categories/list-create'

class CategoryUpdateDeletePageView(TemplateView):
    template_name = 'categories/update-delete.html'
