from django.shortcuts import render
from students.models import *
from lessons.models import *
from course_choice.models import *

def private_room_main_page(request):
    students = Student.objects.filter(user=request.user)
    if len(students) != 0:
        student = students[0]
        all_groups = CourseChoice.objects.filter(student=student,course_group__is_ended=False)
        all_data = []
        for course_group in all_groups:
            course_group = course_group.course_group
            lessons = Lesson.objects.all().filter(course_group=course_group)
            teacher = course_group.user_creator
            data = {
                "student": student,
                "lessons": lessons,
                "teacher": teacher,
                "course_group": course_group,
            }
            all_data.append(data)
        context = {
            "all_data": all_data,
        }
        return render(request, "private_room/main.html", context=context)
    else:
        return render(request, "private_room/admin.html")