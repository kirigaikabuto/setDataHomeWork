from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("register/", register_page, name="register_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", log_out, name="logout"),
]
