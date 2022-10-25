from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import userProfile


class UserProfileForm(UserCreationForm):
    class Meta:
        model = userProfile
        fields = '__all__'
