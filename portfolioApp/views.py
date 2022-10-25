from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EditUserProfileForm


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def edit_userprofile(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have Edited Your Profile Successfully...')
            return redirect('index')

    else:
        form = EditUserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'edit_userprofile.html', context)



