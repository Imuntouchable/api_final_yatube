from rest_framework import permissions


class CreatorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTION']:
            return request.method in permissions.SAFE_METHODS
        return obj.author == request.user
