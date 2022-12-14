"""kartozaTechnicalAssignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolioApp.views import home, profile, login_user, logout_user, edit_userprofile, view_map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('profile', profile, name='profile'),
    path('edit_userprofile/', edit_userprofile, name='edit_userprofile'),
    path('view_map/', view_map, name='view_map'),
]
