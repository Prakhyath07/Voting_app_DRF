from .permissions import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [
        # permissions.IsAdminUser,
        IsStaffEditorPermission]

class UserQuerySetMixin():
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs1 =qs.filter(owner = user)
        qs2 = qs.filter(public = True)
        qsFinal = (qs1 | qs2).distinct()
        return qsFinal

class UserEditSetMixin():
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs1 =qs.filter(owner = user)
        return qs1