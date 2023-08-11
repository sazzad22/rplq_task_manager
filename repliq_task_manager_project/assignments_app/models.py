from django.db import models
from task_manager_app.models import Employee
from task_manager_app.models import Device

# Create your models here.

class Assignments(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
