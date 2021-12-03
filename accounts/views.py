from django.contrib.messages import constants
from django.shortcuts import render, HttpResponse, redirect
import json
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        context = {
            "username": username,
            "email": email
        }

        if User.objects.filter(username=username).first():
            messages.add_message(request, messages.INFO, 'username exist')
            return render(request, "accounts/home.html", context)
        elif User.objects.filter(email=email).first():
            messages.add_message(request, messages.INFO, 'email exist')
            return render(request, "accounts/home.html", context)

        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()

        profile_obj = Profile.objects.create(user=user_obj)
        profile_obj.save()

        return redirect("login")
    else:
        context = {
            "title": "Daily Miles"
        }

        return render(request, 'accounts/home.html', context)


def login(request):
    context = {
        "title": "Daily Miles",
    }
    return render(request, "accounts/login.html", context)
