from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from products.models import Product
from products.serializers import ProductSerializer
from django.views.generic import TemplateView

# api views
class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = []

    def get_queryset(self):
        return Product.objects.all()

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = []

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = []
    lookup_field = 'pk'

    def get_queryset(self):
        return Product.objects.all()

class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = []
    lookup_field = 'pk'

    def get_queryset(self):
        return Product.objects.all()


"""Templates views"""

class ProductListPageView(TemplateView):
    template_name = 'products/list.html'

class ProductCreatePageView(TemplateView):
    template_name = 'products/create.html'

class ProductDetailPageView(TemplateView):
    template_name = 'products/detail.html'

class ProductUpdateDeletePageView(TemplateView):
    template_name = 'products/update-delete.html'