from django.db import models
from django.contrib.auth.models import User
from groups.models import *


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    phone = models.CharField(max_length=255)
    avatar = models.FileField(upload_to="students_avatars/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username