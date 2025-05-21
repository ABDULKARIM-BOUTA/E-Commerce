from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from users.serializers import UserSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination

# class UserListAPIView(ListAPIView):
#     serializer_class = UserListSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsAdminUser]
#     pagination_class = PageNumberPagination
#     pagination_class.page_size = 50


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []

class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
    lookup_field = 'id'