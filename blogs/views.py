from rest_framework import generics
from blogs.models import Blog
from blogs.serializers import BlogSerializer

class BlogListCreate(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = []

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = []
