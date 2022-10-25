from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import userProfile
from .forms import UserProfileForm
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserProfileAdmin(OSMGeoAdmin, UserAdmin):
    model = userProfile
    add_form = UserProfileForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Further details',
            {
                'fields': (
                    'phone_number',
                    'home_address',
                    'location',
                )
            }
        )
    )


admin.site.register(userProfile, UserProfileAdmin)
