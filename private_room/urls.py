from django.urls import path
from .views import *
urlpatterns = [
    path("", private_room_main_page, name="private_room_main_page")
]