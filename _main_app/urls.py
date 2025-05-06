from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('silk/', include('silk.urls', namespace='silk')),

    # first party urls
    path('category/', include('categories.urls')),
    path('product/', include('products.urls')),
    path('order/', include('orders.urls')),
]
