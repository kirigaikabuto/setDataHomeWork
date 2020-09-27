from django.urls import path
from .views import *
urlpatterns = [
    path("", private_room_main_page, name="private_room_main_page"),
    path("schedule/", private_room_schedule_page, name="private_room_schedule_page"),
    path("all_courses/",private_room_all_courses_page, name="private_room_all_courses_page"),
]