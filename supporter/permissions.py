from rest_framework.permissions import BasePermission


class IsSupporterPermissions(BasePermission):
    message = "not access"
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'suporter')

