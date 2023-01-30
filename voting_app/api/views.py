from rest_framework import generics, permissions, response
from django.contrib.auth import login, logout
from api.mixins import UserQuerySetMixin, StaffEditorPermissionMixin
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from .authentication import TokenAuthentication
# from.models import Users

# Create your views here.
## listcreate does both list and create
class UserCreate(
    # UserQuerySetMixin,
    # StaffEditorPermissionMixin,
    generics.CreateAPIView):

    queryset = User.objects.all()
    
    serializer_class = RegisterSerializer

    permission_classes = [permissions.AllowAny]

class LoginApi(
    generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    def post(self,request):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return redirect(reverse("poll:Poll-list"))

#Logout
def user_logout(request):
    logout(request)
    return redirect(reverse("api:User-login"))

