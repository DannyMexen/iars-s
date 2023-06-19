from django.db import models

# Create your models here.

# Notifications
class Notification(models.Model):
    name = models.CharField(unique=True,max_length=100,null=False)
    description = models.TextField(max_length=300,null=False)

# Change Reasons
class ChangeReason(models.Model):
    name = models.CharField(unique=True,max_length=100,null=False)
    description = models.TextField(max_length=300,null=False)