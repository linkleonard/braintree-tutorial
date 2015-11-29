from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.payer == request.user


class AnonymousCanCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        return view.action == 'create'
