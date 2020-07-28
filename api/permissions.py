from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user.role == 'admin' and request.user.is_staff)