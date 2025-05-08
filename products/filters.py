import django_filters
from products.models import Product

class ProductFilters(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains') # filter by category name

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price': ['exact', 'lt', 'gt', 'range'],
        }