import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager For User Profiles"""
    def create_user(self, email, name, password=None):
        """Create a new User Profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        #user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
         """create and save a new  super user witg given details"""
         user = self.create_user(email= email, name= name, password= password)

         user.is_superuser = True
         user.is_staff = True
         user.save(self._db)

         return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_user_name(self):
        """retrive full name of user"""
        return self.name

    def get_short_name(self):
        """retrive short name of user"""
        return self.name


    def __str__(self):
        """return string representation of our user"""
        return self.email

