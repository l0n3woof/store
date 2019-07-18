from django.db import models

# Create your models here.
class UserDetails(models.Model):
    full_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    store_name = models.CharField(max_length=80)
    address_line1 = models.CharField(max_length=80)
    address_line2 = models.CharField(max_length=80)
    pin_code = models.CharField(max_length=80)
    district = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    pan_number = models.CharField(max_length=80)
    gst_number = models.CharField(max_length=80)
