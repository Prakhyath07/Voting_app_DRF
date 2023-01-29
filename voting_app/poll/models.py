from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Parties(models.Model):
    party = models.CharField(max_length=128,
    validators=[MinLengthValidator(1, "Title must be greater than 1 characters")])

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.party


class Poll(models.Model):
    # name = models.CharField(max_length=128,
    #                 validators=[MinLengthValidator(2, "Title must be greater than 2 characters")])
    voted= models.ForeignKey('Parties', on_delete=models.CASCADE, null=False)


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

