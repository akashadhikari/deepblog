from rest_framework import generics

from .models import Tag, Post
from .serializers import TagSerializer, PostSerializer


class TagListViewSet(generics.ListCreateAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostListViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
