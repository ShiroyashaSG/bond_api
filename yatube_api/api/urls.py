from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('groups', GroupViewSet)
router_v1.register('posts', PostViewSet)
router_v1.register('follow', FollowViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
