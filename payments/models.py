from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments') # an order can have multiple payments
    method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100) # to store ids from external services like Paypal
    created_at = models.DateTimeField(auto_now_add=True)

class Refund(models.Model):
    # REFUND_STATUS_CHOICES = [
    #     ('pending', 'Pending'),
    #     ('approved', 'Approved'),
    #     ('rejected', 'Rejected'),
    #     ('processed', 'Processed'),
    # ]

    # Optional Additions
    #
    # Link to Payment if multiple payments per order
    # is_partial boolean(vs full refunds
    # refunded_by(admin user or staff account)
    # document upload(e.g., bank slip, receipt)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='refunds')
    reason = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True) # should be specified by the admin
    status = models.CharField(max_length=25)

    def __str__(self):
        return f"Refund for Order #{self.order.id} - {self.status}"