from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models


# Create your models here.

class userProfile(AbstractUser):
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    user_name = models.CharField('username', max_length=30, blank=True)
    address = models.CharField('street address', max_length=30, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)

    class Meta:
        db_table = 'UserProfile'

