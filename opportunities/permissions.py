from rest_framework import permissions

class IsAdminOrUserCreateOnly(permissions.BasePermission):
    """
    Custom permission to allow:
    - Authenticated users to create (POST) applications.
    - Only admins to perform other actions (GET, PUT, DELETE).
    """

    def has_permission(self, request, view):
        # Allow POST for all authenticated users
        if request.method == 'POST':
            return request.user.is_authenticated

        # Allow all actions for admins only
        return request.user.is_staff
 