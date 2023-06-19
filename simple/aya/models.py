from django.db import models

# Create your models here.


# A. Standalone tables - no relationships
# Notifications
class Notification(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=300)


# Change reasons
class ChangeReason(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=300)


# B. Users
# User roles
class UserRole(models.Model):
    ADMINISTRATOR = "AD"
    STANDARD = "ST"
    ROLE_CHOICES = [
        (ADMINISTRATOR, "Administrator"),
        (STANDARD, "Standard"),
    ]
    name = models.CharField(
        unique=True,
        default=STANDARD,
        choices=ROLE_CHOICES,
    )

    STD_DESCRIPTION = "Standard user - core system access privileges."
    # ADMIN_DESCRIPTION = "Administrator  - elevated system access privileges."
    description = models.TextField(max_length=300, default=STD_DESCRIPTION)


# User account statuses
class UserAccountStatus(models.Model):
    ACTIVE = "AC"  # Enabled and in use
    INACTIVE = "IA"  # Not in use but accessible
    DISABLED = "DI"  # Requires activation to use
    ARCHIVED = "AR"  # Completely unusable and cannot be activated
    ACCOUNT_STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
        (DISABLED, "Disabled"),
        (ARCHIVED, "Archived"),
    ]
    name = models.CharField(
        unique=True,
        default=ACTIVE,
        choices=ACCOUNT_STATUS_CHOICES,
    )
    description = models.TextField(max_length=300)


# Users
class User(models.Model):
    login_name = models.CharField(max_length=100, unique=True)
    password_hash = models.TextField(max_length=500, unique=True)
    user_account_status_id = models.ForeignKey(UserAccountStatus, on_delete=models.RESTRICT)
    user_role_id = models.ForeignKey(UserRole, on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=13, unique=True) # TODO: PhoneNumberField
    email = models.EmailField(max_length=254, unique=True)

 # C. Log and Events
 # Event

class Event(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=300)

# Log
class Log(models.Model):
    EVENT_ID = 0
    event_id = models.ForeignKey(Event, on_delete=models.RESTRICT, default=EVENT_ID)
    USER_ID = 0
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, default=USER_ID)
    date = models.DateTimeField(auto_now=True)
    EVENT = "Event Logged " + str(date)
    details = models.TextField(max_length=400, default=EVENT)

# D. Organizations
# Provinces
class Province(models.Model):
    # Source (Not Secure) - http://www.statoids.com/uzm.html
    CENTRAL = "CE"
    COPPERBELT = "CO"
    EASTERN = "ES"
    LUAPULA = "LP"
    LUSAKA = "LS"
    MUCHINGA = "MU"
    NORTHERN = "NR"
    NORTH_WESTERN = "NW"
    WESTERN = "WE"
    SOUTHERN = "SO"
    PROVINCE_CHOICES = [
        (CENTRAL, "Central"),
        (COPPERBELT, "Copperbelt"),
        (EASTERN, "Eastern"),
        (LUAPULA, "Luapula"),
        (LUSAKA, "Lusaka"),
        (MUCHINGA, "Muchinga"),
        (NORTHERN, "Northern"),
        (NORTH_WESTERN, "North Western"),
        (WESTERN, "Western"),
        (SOUTHERN, "Southern")
    ]
    name = models.CharField(
        choices=PROVINCE_CHOICES,
        default=CENTRAL
    )

# Cities
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)