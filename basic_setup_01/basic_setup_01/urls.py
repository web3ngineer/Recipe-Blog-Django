"""
URL configuration for basic_setup_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from home.views import *
from authentication.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.main, name='main'),
    path('layout/', views.layout, name='layout'),

    # calling views from app in base app urls
    path('home1/', home1, name='home1'),
    # path('home/', home, name='home'),
    path('auth/signin/', signin, name='signin'),
    path('auth/signup/', signup, name='signup'),
    path('auth/signout/', signout, name='signout'),
    path('auth/changepassword/', changepassword, name='changepassword'),
    path('auth/profile/', profile, name='profile'),

    # including app url in base app url
    path('home/', include('home.urls')),
    path('auth/', include('authentication.urls')),
    path('receipe/', include('recipeProject.urls')),
]

