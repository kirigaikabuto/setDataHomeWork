from django.shortcuts import render
from students.models import *
from lessons.models import *


def private_room_main_page(request):
    students = Student.objects.filter(user=request.user)
    if len(students) != 0:
        student = students[0]
        lessons = Lesson.objects.all().filter(course_group=student.group)
        teacher = student.group.user_creator
        context = {
            "student": student,
            "lessons": lessons,
            "teacher": teacher,
        }
        return render(request, "private_room/main.html", context=context)
    else:
        return render(request, "private_room/admin.html")