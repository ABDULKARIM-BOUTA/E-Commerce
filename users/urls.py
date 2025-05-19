from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import UserDetailView, UserCreateView

urlpatterns = [
    # JWT urls
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API urls
#    path('api/list/', UserListAPIView.as_view(), name='api-user-list'),
    path('api/<int:pk>/detail/', UserDetailView.as_view(), name='api-user-detail'),

]