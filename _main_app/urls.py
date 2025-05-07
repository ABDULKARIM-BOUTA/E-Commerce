from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),

    # third party urls
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # first party urls
    path('category/', include('categories.urls')),
    path('product/', include('products.urls')),
    path('order/', include('orders.urls')),
    path('user/', include('users.urls')),
]
