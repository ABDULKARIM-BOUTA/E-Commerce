from django.db import models

class Tax(models.Model):
    name = models.CharField(max_length=100)  # ex: VAT
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True, blank=True)

    # region = models.CharField(max_length=100, blank=True, null=True)
    # is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     unique_together = ('name', 'country', 'region')
    #
    # def __str__(self):
    #     return f"{self.name} ({self.rate}%)"
