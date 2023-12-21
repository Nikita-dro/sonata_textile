from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
