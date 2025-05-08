from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from products.models import Product
from products.serializers import ProductSerializer
from django.views.generic import TemplateView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from  products.filters import ProductFilters

# api views
class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    search_fields = ['=name', 'category__name', 'description']
    filterset_class = ProductFilters
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['name']  # default order

    def get_queryset(self):
        # product is not listed if out od stock
        return Product.objects.prefetch_related('category').filter(stock_quantity__gt=0)

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Product.objects.all()

    def get_permissions(self):
        method = self.request.method
        self.permission_classes = [AllowAny]

        if method in ['PUT', 'DELETE', 'PATCH']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

"""Templates views"""

class ProductListPageView(TemplateView):
    template_name = 'products/list.html'

class ProductCreatePageView(TemplateView):
    template_name = 'products/create.html'

class ProductDetailUpdateDeletePageView(TemplateView):
    template_name = 'products/update-delete.html'