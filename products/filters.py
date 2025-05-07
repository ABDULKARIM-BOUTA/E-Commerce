import django_filters
from products.models import Product

class ProductFilters(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['exact', 'lt', 'gt', 'range'],
            'category': ['exact']
        }
