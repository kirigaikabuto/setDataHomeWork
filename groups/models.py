from django.db import models
from courses.models import *
from django.contrib.auth.models import User


class CourseGroup(models.Model):
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_ended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name + "->" + self.name
