from django.urls import path
from .views import *

urlpatterns = [
    path("lesson_detail/<int:pk>/", lesson_detail, name="lesson_detail"),
]