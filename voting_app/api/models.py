# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser
# # Create your models here.

# class MyAccountManager(BaseUserManager):


#     def create_user(self, username, fullname=None, password=None
#                     ):
#         if not username:
#             raise ValueError('Users must have an username')

#         user = self.model(
#             username =username,
#             name=fullname,
#         )


#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password):
#         user = self.create_user(
#             username=self.normalize_email(username),
#             password=password,
#         )
#         user.is_admin = True
#         user.is_active=True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

# class Users(AbstractUser):
#     Email_Address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
#     name = models.CharField(max_length=30, blank=True, null=True)
#     username= models.CharField(max_length=30,unique=True, blank=True, null=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'username'

#     # objects = MyAccountManager()

#     class Meta:
#         db_table = "tbl_users"

#     def __str__(self):
#         return str(self.username)


    
