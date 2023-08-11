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


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    

class Device(models.Model):
    device_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    

class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    condition_at_assignment = models.CharField(max_length=100)
    

class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    log_date = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=100)