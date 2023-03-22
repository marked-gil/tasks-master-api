from rest_framework import permissions


class IsAuthenticatedReadOnly(permissions.BasePermission):
    """ Read-only permission for authenticated users """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method \
                in permissions.SAFE_METHODS:
            return True


class IsOwner(permissions.BasePermission):
    """ Custom permission for instance owner """
    message = 'Access denied.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
