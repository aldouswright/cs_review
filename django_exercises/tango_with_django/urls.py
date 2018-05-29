"""django_exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import tango_with_django.views as twd_views

app_name = "twd"

urlpatterns = [
    path("home/", twd_views.index, name="home"),
    path("login/", twd_views.login, name="login"),
    path("user_profile/", twd_views.profile, name="user_profile"),
    path("create_page/", twd_views.create, name="create_page"),
    path("track_url/", twd_views.track_url, name="track"),
    path("page_detail/", twd_views.page_detail, name="page_detail")
]
