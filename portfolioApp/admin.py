from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import userProfile


# Register your models here.
# admin.site.register(userProfile)
class UserProfileAdmin(OSMGeoAdmin):
    pass


admin.site.register(userProfile, UserProfileAdmin)
