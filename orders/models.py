import uuid
from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator

User = get_user_model()

class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
        DELIVERED = 'Delivered'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders') # to reference in user history orders
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')
    address = models.TextField()
#    payment_method = models.CharField(max_length=50, choices=PaymentChoices.choices)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'#Order: {self.order_id} by {self.user}'

class OrderItem(models.Model):
    """used as an intermediate class that connects products and orders while adding extra details like quantity and item total price"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def item_total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f' #Order: {self.order.order_id} (Price: {self.product.price} x Quantity: {self.quantity})'