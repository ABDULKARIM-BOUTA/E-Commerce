from django.db.models.signals import post_delete, post_save
from django.core.cache import cache
from django.dispatch import receiver
from products.models import Product

# @receiver([post_delete, post_save], sender=Product)
# def invalidate_product_list_cache(sender, instance, **kwargs):
#     """ invalidate product list cache if the an item was added, updated, or deleted """
#
#     print('Casche was cleared')
#     cache.delete_pattern('*product_list*')