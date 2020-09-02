from django.db import models
from groups.models import *
import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
from students.models import Student

class Lesson(models.Model):
    course_group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    materials = models.FileField(upload_to="lessons_materials/", default=None)
    path_to_video_lesson = models.CharField(max_length=255, default="")
    planning_date = models.DateTimeField(default=now)
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.course_group.name + "->" + self.name


class Comment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.student.user.username+ "->" + self.lesson.name + "->" + self.message