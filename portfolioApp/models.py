from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class userProfile(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    home_address = models.CharField('Home address', max_length=30, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)

    class Meta:
        db_table = 'UserProfile'
