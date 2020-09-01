from django.db import models
from django.contrib.auth.models import User
from groups.models import *


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    phone = models.CharField(max_length=255)
    avatar = models.FileField(upload_to="students_avatars/")
    group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
