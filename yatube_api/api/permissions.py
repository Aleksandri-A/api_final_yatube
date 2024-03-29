from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class AuthorPOSTGet(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                request.method == "POST" or request.method == "GET"
            )
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
