from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .user_manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company_name']

    def __str__(self):
        return self.email,self.company_name