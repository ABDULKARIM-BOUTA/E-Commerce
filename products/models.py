from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from categories.models import Category
from vendors.models import Vendor
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(1)])
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    slug = models.SlugField(max_length=50)

    @property
    def check_in_stock(self):
        return self.stock_quantity > 0

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.product} ({self.rating} stars)"

