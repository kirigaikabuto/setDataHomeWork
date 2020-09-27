from django.shortcuts import render
from .models import *
from users.models import *


def lesson_detail(request, pk):
    student = Student.objects.get(user=request.user)
    lesson = Lesson.objects.get(pk=pk)
    if request.method == "POST":
        message = request.POST['message']
        comment = Comment(lesson=lesson, student=student, message=message)
        comment.save()
    teacher = lesson.course_group.user_creator
    profile = UserProfile.objects.get(user=teacher)
    comments = Comment.objects.filter(lesson=lesson)
    context = {
        "lesson": lesson,
        "teacher": teacher,
        "profile": profile,
        "comments": comments,
    }
    return render(request, "lessons/lesson_detail.html", context=context)
