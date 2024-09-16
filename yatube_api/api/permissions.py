from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Кастомное разрешение, которое позволяет редактировать объект только
    его автору."""

    def has_object_permission(self, request, view, obj):
        """Проверяет, имеет ли пользователь права на выполнение данного
        запроса с объектом."""

        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
