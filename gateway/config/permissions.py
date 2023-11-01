from rest_framework.permissions import BasePermission


class IsAuthencicatedAndOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user_svc)

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)