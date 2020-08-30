from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to="courses_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

