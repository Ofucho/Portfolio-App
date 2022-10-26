from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def edit_userprofile(request):
    return render(request, 'edit_userprofile.html')

