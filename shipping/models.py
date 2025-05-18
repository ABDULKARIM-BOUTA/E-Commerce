from django.db import models

class Shipping(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_delivery_time = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)