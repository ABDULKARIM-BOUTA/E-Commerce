from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from users.serializers import UserListSerializer, UserDetailSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 50

class UserDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'