from django.contrib.gis.db.models.functions import AsGeoJSON
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.serializers import serialize


# Create your models here.

class userProfile(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    home_address = models.CharField('Home address', max_length=30, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)

    class Meta:
        db_table = 'UserProfile'

    def allUploads(self):
        """ Returns all objects from the database as a geojson"""
        return self.objects.annotate(geometry=AsGeoJSON('location'))
    @classmethod
    def serialized(cls):
        """returns all the uploads in a serialized format"""
        print(cls.objects.all())
        return serialize('geojson', cls.objects.all())
