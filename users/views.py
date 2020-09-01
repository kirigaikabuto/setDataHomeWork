from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout


def register_page(request):
    user_form = None
    profile_form = None
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileCreationForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            my_user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = my_user
            profile.save()
            return redirect("main_page")
    user_form = UserCreationForm()
    profile_form = UserProfileCreationForm()
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "users/register_page.html", context=context)


def login_page(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) == 0 or len(password) == 0:
            error = "Заполните все поля"
        else:
            user = authenticate(request, username=username, password=password)
            if user is None:
                error = "нет такого пользователя"
            else:
                login(request, user)
                return redirect("main_page")
    context = {
        "error": error
    }
    return render(request, "main/index.html", context=context)


def log_out(request):
    logout(request)
    return redirect("main_page")