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
    #status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')
    shipping_address = models.TextField()
    #payment_method = models.CharField(max_length=50, choices=PaymentChoices.choices)
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

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)





# class Subscription(models.Model):
#     STATUS_CHOICES = [
#         ('active', 'Active'),
#         ('paused', 'Paused'),
#         ('cancelled', 'Cancelled'),
#         ('expired', 'Expired'),
#     ]
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subscriptions')  # Subscribed product
#     quantity = models.PositiveIntegerField(default=1)
#     start_date = models.DateField(auto_now_add=True)
#     next_delivery_date = models.DateField()
#     frequency = models.CharField(
#         max_length=20,
#         choices=[('weekly', 'Weekly'), ('biweekly', 'Biweekly'), ('monthly', 'Monthly')],
#         default='monthly'
#     )
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
#     auto_renew = models.BooleanField(default=True)
#     last_billed = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.user.email} - {self.product.name} ({self.frequency})"
#
#     def is_active(self):
#         return self.status == 'active'

# class Coupon(models.Model):
#     code = models.CharField(max_length=50, unique=True)
#     description = models.TextField(blank=True, null=True)
#     discount_type = models.CharField(max_length=10, choices=[('fixed', 'Fixed'), ('percent', 'Percent')])
#     discount_value = models.DecimalField(max_digits=10, decimal_places=2)
#     active = models.BooleanField(default=True)
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     usage_limit = models.PositiveIntegerField(blank=True, null=True)  # max number of uses
#     used_count = models.PositiveIntegerField(default=0)
#
#     def is_valid(self):
#         now = timezone.now()
#         return (
#             self.active and
#             self.valid_from <= now <= self.valid_to and
#             (self.usage_limit is None or self.used_count < self.usage_limit)
#         )
#
#     def __str__(self):
#         return self.code