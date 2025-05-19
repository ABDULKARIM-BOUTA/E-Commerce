from django.db import models
from products.models import Product

class Analytics(models.Model):
    """ sales summary for each month """
    
    popular_products = models.ManyToManyField(Product, related_name='analytics')
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    traffic = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # label = models.CharField(max_length=50) # ex: May 2025
    # orders_count = models.PositiveIntegerField(default=0)