from django.db import models
from groups.models import *


class Lesson(models.Model):
    course_group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    materials = models.FileField(upload_to="lessons_materials/", default=None)
    path_to_video_lesson = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.course_group.name + "->" + self.name