from .permissions import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

class UserQuerySetMixin():
    user_field = 'owner'
    is_public = "public"
    allow_staff_view = True
    def get_queryset(self):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        
        qs = super().get_queryset()
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)