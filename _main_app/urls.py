from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),

    # third party urls
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),

    # first party urls
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('analytics/', include('analytics.urls')),
    path('blogs/', include('blogs.urls')),
    path('carts/', include('carts.urls')),
    path('configuration/', include('configuration.urls')),
    path('notifications/', include('notifications.urls')),
    path('payments/', include('payments.urls')),
    path('shipping/', include('shipping.urls')),
    path('support/', include('support.urls')),
    path('taxes/', include('taxes.urls')),
    path('vendors/', include('vendors.urls')),
    path('wishlists/', include('wishlists.urls')),
]
