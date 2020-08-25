from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        print(request.user)
        if request.method in SAFE_METHODS:
            print('se hace una petición tipo SAFE_METHODS...')
            return True
        else:
            print('se hace una petición distinta a SAFE_METHODS...')
            return request.user.is_staff


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.created_by == request.user