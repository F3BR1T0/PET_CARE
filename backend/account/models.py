from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from uuid import uuid4

class AppAccountManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        email = self.normalize_email(email)
        user = self.model(email = email, username=username)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username,password=None):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user
    
class AppAccount(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppAccountManager()
    
    def __str__(self):
        return self.username