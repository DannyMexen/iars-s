from django.db import models

# Create your models here.

# A. Standalone tables - no relationships
# Notifications
class Notification(models.Model):
    name = models.CharField(unique=True,max_length=100,null=False)
    description = models.TextField(max_length=300,null=False)

# Change Reasons
class ChangeReason(models.Model):
    name = models.CharField(unique=True,max_length=100,null=False)
    description = models.TextField(max_length=300,null=False)

# B. User Roles
class UserRole(models.Model):
    ADMINISTRATOR = "AD"
    STANDARD = "ST"
    ROLE_CHOICES = [
        (ADMINISTRATOR, "Administrator"),
        (STANDARD, "Standard"),
    ]
