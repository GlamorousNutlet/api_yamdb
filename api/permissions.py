from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return bool(request.user and request.user.is_staff)
        else:
            if request.user.is_authenticated:
                if request.user.role == 'admin' or request.user.role == 'django_adm':
                    return True
