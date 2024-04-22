from django.shortcuts import render
from rest_framework import generics
from .models import PostBlog
from .serializers import PostBlogSerializer


class PostBlogListCreate(generics.ListCreateAPIView):
    queryset = PostBlog.objects.all()
    serializer_class = PostBlogSerializer