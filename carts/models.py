import msilib

from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True) # allow non users to create a cart
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f'#Cart: {self.session_id} by {self.user}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f' #Order: {self.cart.session_id} (Price: {self.product.price} x Quantity: {self.quantity})'
