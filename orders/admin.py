from django.contrib import admin
from orders.models import Order, OrderItem, Coupon, Subscription

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon)
admin.site.register(Subscription)