from .models import Users
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        Email_Address = serializers.EmailField()
        password = serializers.CharField(
                     style={'input_type': 'password'}
                    )
        fields = [
            "username",
            "name",
            "Email_Address",
            "password",

        ]
        
        
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
                
            password = self.validated_data["password"]
            self.set_password(password)
            self.save()
