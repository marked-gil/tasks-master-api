from rest_framework import permissions


class IsOwnerIsAuthenticated(permissions.BasePermission):
    """
    Custom permission to allow update and delete to the owner only,
    while allowing read-only access to other authenticated users
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
