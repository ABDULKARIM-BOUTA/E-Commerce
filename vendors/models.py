from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    store_description = models.TextField()
    store_name = models.CharField(max_length=100)
    bank_details = models.TextField()
    store_logo = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField()
    contact_details = models.TextField()
    shipping_policy = models.TextField()
    refund_policy = models.TextField()

    def __str__(self):
        return self.store_name