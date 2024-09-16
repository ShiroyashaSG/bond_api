from rest_framework import mixins
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .permissions import IsAuthorOrReadOnly
from posts.models import Group, Post, Follow
from .serializers import (
    PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
)

User = get_user_model()


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Представление предоставляющее create()` и `list()` по умолчанию."""


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление для просмотра групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """Представление для просмотра и редактирования постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Сохраняет пост с текущим пользователем в качестве автора."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для просмотра и редактирования комментариев к постам."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & IsAuthorOrReadOnly]

    def get_post(self):
        """Получает пост, к которому принадлежит комментарий."""
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def perform_create(self, serializer):
        """Сохраняет комментарий с текущим пользователем в качестве автора
        и связывает его с постом.
        """
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )

    def get_queryset(self):
        """Возвращает комментарии для указанного поста."""
        return self.get_post().comments.all()


class FollowViewSet(CreateListViewSet):
    """Представление для просмотра и добавления подписчиков пользователя."""
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        """Возвращает подписчиков для указанного пользователя."""
        user = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        """Сохраняет подписчика для текущего пользователя."""
        serializer.save(user=self.request.user)
