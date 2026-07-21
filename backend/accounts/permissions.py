from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Authenticated users can read.
    Only admins can create, update and delete.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsAdmin(BasePermission):
    """
    Allows access only to admins.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )