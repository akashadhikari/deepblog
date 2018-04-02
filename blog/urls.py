from django.urls import path

from .views import TagListViewSet, TagDetailsViewSet, PostListViewSet, PostDetailsViewSet

urlpatterns = [

    path('tag/', TagListViewSet.as_view(), name="tag_list"),
    path('tag/<int:pk>/', TagDetailsViewSet.as_view(), name='tag_detail'),

    path('post/', PostListViewSet.as_view(), name="post_blog_list"),
    path('post/<int:pk>/', PostDetailsViewSet.as_view(), name='post_blog_detail'),
]

"""
@TODO
1) Permissions
2) Blog URL: /<user>/<slug:title>

"""
