from rest_framework import generics, permissions

from api.mixins import UserQuerySetMixin, StaffEditorPermissionMixin

from .serializers import RegistrationSerializer

from.models import Users

# Create your views here.
## listcreate does both list and create
class UserCreate(
    # UserQuerySetMixin,
    # StaffEditorPermissionMixin,
    generics.CreateAPIView):

    queryset = Users.objects.all()
    
    serializer_class = RegistrationSerializer

    permission_classes = [permissions.AllowAny]


