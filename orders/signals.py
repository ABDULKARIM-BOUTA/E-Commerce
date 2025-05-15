from orders.models import Order
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

@receiver([post_delete, post_save], sender=Order)
def invalidate_orders_list_cache(sender, instance, **kwargs):
    """ invalidate admin's orders list cache when modified """

    print('Cache was cleared')
    cache.delete_pattern('*admin_order_list*')