<<<<<<< HEAD
<<<<<<< HEAD
import datetime

from django.db import models
from django.utils import timezone

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
    user_role = models.ForeignKey(UserRole, on_delete=models.RESTRICT)
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
    event = models.ForeignKey(Event, on_delete=models.RESTRICT, default=EVENT_ID)
    USER_ID = 0
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=USER_ID)
    date = models.DateTimeField(auto_now_add=True)
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

# Clients
class Client(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT) # TODO: Consider SET DEFAULT
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_phone_number = models.CharField(max_length=13, unique=True)
    contact_email = models.EmailField(max_length=254, unique=True)

# AMWS (replace with your own organization's name)
class ArcariusMexen(models.Model):
    name = models.CharField(max_length=200)
    tpin = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT) # TODO: Consider SET DEFAULT
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_phone_number = models.CharField(max_length=13, unique=True)
    contact_email = models.EmailField(max_length=254, unique=True)

# E. Invoices and Receipts
# Bank account types
class BankAccountType(models.Model):
    CURRENT = "CU"
    SAVINGS = "SA"
    ACCOUNT_TYPE_CHOICES = [
        (CURRENT, "Current"),
        (SAVINGS, "Savings"),
    ]
    name = models.CharField(
        choices=ACCOUNT_TYPE_CHOICES,
        default=CURRENT,
        unique=True,
    )

# Banks
class Bank(models.Model):
    name = models.CharField(max_length=200)
    account_type = models.ForeignKey(BankAccountType, on_delete=models.RESTRICT)
    swift_code = models.CharField(max_length=11, unique=True)
    branch_name = models.CharField(max_length=100)

# Payment conditions
class PaymentCondition(models.Model):
    name = models.CharField(max_length=150, unique=True) # TODO: choices!
    description = models.TextField(max_length=300)

# Service
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True) # TODO: choices!
    description = models.TextField(max_length=300)
    cost = models.DecimalField(max_digits=6, decimal_places=4)

# Invoice
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=10, unique=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=4)
    payment_condition = models.ForeignKey(PaymentCondition, on_delete=models.RESTRICT)
    bank = models.ForeignKey(Bank, on_delete=models.RESTRICT)
    issue_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=30))

# Invoice items
class InvoiceItem(models.Model):
    item_number = models.CharField(max_length=10, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    AMOUNT = 0
    total_amount = models.DecimalField(max_digits=6, decimal_places=4, default=AMOUNT)

# Receipts
class Receipt(models.Model):
    receipt_number = models.CharField(max_length=10, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

# Receipt items
class ReceiptItems(models.Model):
    receipt_number = models.CharField(max_length=10, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE)
=======
=======
import datetime

>>>>>>> 976d4b3 (parent f00e79fd1cf10d05707b207118291cf98900e568)
from django.db import models
from django.utils import timezone

# Create your models here.
<<<<<<< HEAD
>>>>>>> f00e79f (# This is a combination of 6 commits.)
=======


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
    user_role = models.ForeignKey(UserRole, on_delete=models.RESTRICT)
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
    event = models.ForeignKey(Event, on_delete=models.RESTRICT, default=EVENT_ID)
    USER_ID = 0
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=USER_ID)
    date = models.DateTimeField(auto_now_add=True)
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

# Clients
class Client(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT) # TODO: Consider SET DEFAULT
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_phone_number = models.CharField(max_length=13, unique=True)
    contact_email = models.EmailField(max_length=254, unique=True)

# AMWS (replace with your own organization's name)
class ArcariusMexen(models.Model):
    name = models.CharField(max_length=200)
    tpin = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT) # TODO: Consider SET DEFAULT
    contact_first_name = models.CharField(max_length=100)
    contact_last_name = models.CharField(max_length=100)
    contact_phone_number = models.CharField(max_length=13, unique=True)
    contact_email = models.EmailField(max_length=254, unique=True)

# E. Invoices and Receipts
# Bank account types
class BankAccountType(models.Model):
    CURRENT = "CU"
    SAVINGS = "SA"
    ACCOUNT_TYPE_CHOICES = [
        (CURRENT, "Current"),
        (SAVINGS, "Savings"),
    ]
    name = models.CharField(
        choices=ACCOUNT_TYPE_CHOICES,
        default=CURRENT,
        unique=True,
    )

# Banks
class Bank(models.Model):
    name = models.CharField(max_length=200)
    account_type = models.ForeignKey(BankAccountType, on_delete=models.RESTRICT)
    swift_code = models.CharField(max_length=11, unique=True)
    branch_name = models.CharField(max_length=100)

# Payment conditions
class PaymentCondition(models.Model):
    name = models.CharField(max_length=150, unique=True) # TODO: choices!
    description = models.TextField(max_length=300)

# Service
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True) # TODO: choices!
    description = models.TextField(max_length=300)
    cost = models.DecimalField(max_digits=6, decimal_places=4)

# Invoice
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=10, unique=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=4)
    payment_condition = models.ForeignKey(PaymentCondition, on_delete=models.RESTRICT)
    bank = models.ForeignKey(Bank, on_delete=models.RESTRICT)
    issue_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=30))

# Invoice items
class InvoiceItem(models.Model):
    item_number = models.CharField(max_length=10, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    AMOUNT = 0
    total_amount = models.DecimalField(max_digits=6, decimal_places=4, default=AMOUNT)

# Receipts
class Receipt(models.Model):
    receipt_number = models.CharField(max_length=10, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

# Receipt items
class ReceiptItems(models.Model):
    receipt_number = models.CharField(max_length=10, unique=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    invoice_item = models.ForeignKey(InvoiceItem, on_delete=models.CASCADE)
>>>>>>> 976d4b3 (parent f00e79fd1cf10d05707b207118291cf98900e568)
