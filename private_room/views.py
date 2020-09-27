from django.shortcuts import render
from students.models import *
from lessons.models import *
from course_choice.models import *
from datetime import timedelta
from django.utils import timezone


def private_room_main_page(request):
    students = Student.objects.filter(user=request.user)
    some_day_next_week = timezone.now().date() + timedelta(days=7)
    monday_of_next_week = some_day_next_week + timedelta(days=(some_day_next_week.isocalendar()[2] - 6))
    monday_of_this_week = monday_of_next_week - timedelta(days=7)
    print(monday_of_this_week)
    print(monday_of_next_week)
    if len(students) != 0:
        student = students[0]
        all_groups = CourseChoice.objects.filter(student=student, course_group__is_ended=False)
        all_data = []
        for course_group in all_groups:
            course_group = course_group.course_group
            lessons = Lesson.objects.all().filter(course_group=course_group, planning_date__gte=monday_of_this_week,
                                                  planning_date__lt=monday_of_next_week)
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
