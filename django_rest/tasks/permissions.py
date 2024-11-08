from rest_framework import permissions

class IsProjectManagerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['PROJECT_MANAGER', 'ADMIN']

class IsTaskOwnerOrProjectManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ['PROJECT_MANAGER', 'ADMIN']:
            return True
        
        return obj.created_by == request.user or obj.assigned_to == request.user
