from django.shortcuts import render
from students.models import *


def private_room_main_page(request):
    student = Student.objects.get(user=request.user)
    context = {
        "student": student
    }
    return render(request, "private_room/main.html", context=context)