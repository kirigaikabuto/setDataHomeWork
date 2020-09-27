from django.db import models
from students.models import *
from groups.models import *


class CourseChoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_group = models.ForeignKey(CourseGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.user.username + "->" + self.course_group.__str__()