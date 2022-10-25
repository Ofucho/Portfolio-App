from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import userProfile
from django.contrib.auth.models import User


class UserProfileForm(UserCreationForm):
    class Meta:
        model = userProfile
        fields = '__all__'


class EditUserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
