# from .models import Users
from rest_framework import serializers
from django.contrib.auth.models import User

# class RegistrationSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Users
#         Email_Address = serializers.EmailField()
#         password = serializers.CharField(
#                      style={'input_type': 'password'}
#                     )
#         fields = [
#             "username",
#             "name",
#             "Email_Address",
#             "password",

#         ]
        
        
#         extra_kwargs = {"password": {"write_only": True}}

#         def create(self, validated_data):
                
#             password = self.validated_data["password"]
#             self.set_password(password)
#             self.save()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Register Serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}