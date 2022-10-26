from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EditUserProfileForm
from .models import userProfile
from django.core.serializers import serialize
import folium, geojson
from folium.features import GeoJsonPopup, GeoJsonTooltip


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


def view_map(request):
    location_as_geojson = serialize('geojson', userProfile.objects.all())
    print(location_as_geojson)
    m = folium.Map()

    # popup = GeoJsonPopup(
    #     fields=["first_name", "last_name"],
    #     aliases=["Parcel id :", "Owner id :", ],
    #     localize=True, labels=True,
    #     )

    geo = folium.GeoJson(location_as_geojson, name="geojson").add_to(m)

    folium.features.GeoJsonPopup(fields=["phone_number", "home_address","username","first_name", "last_name", "email"]).add_to(geo)


    # popup.add_to(geo)


    m = m._repr_html_()

    context = {

        'm': m,
    }
    return render(request, 'map.html', context)
