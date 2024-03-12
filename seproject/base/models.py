from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other employee details here
    def enter(self):
        EntryExitRecord.objects.create(employee=self)

    def exit(self):
        record = EntryExitRecord.objects.filter(employee=self, exit_time__isnull=True).latest('entry_time')
        record.exit_time = datetime.now()
        record.save()

class EntryExitRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)