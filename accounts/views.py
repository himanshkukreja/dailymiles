from django.contrib.messages import constants
from django.shortcuts import render, HttpResponse, redirect
import json
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as logt
from django.contrib.auth import authenticate, login as lg


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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        context = {
            "username": username,
            "password": password
        }

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.add_message(request, messages.INFO, 'Username not found')
            return render(request, "accounts/login.html", context)

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj:
            messages.add_message(request, messages.INFO,
                                 'No such accont exists')
            return render(request, "accounts/login.html", context)

        user = authenticate(username=username, password=password)

        if user is None:
            messages.add_message(request, messages.INFO, 'Wrong password')
            return render(request, "accounts/login.html", context)

        lg(request, user)
        return redirect('dashboard')
    else:
        context = {
            "title": "Daily Miles",
        }

        return render(request, "accounts/login.html", context)


def logout(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logt(request)
    return redirect("login")


def data(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        age = request.POST.get("age")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        sex = request.POST.get("sex")

        obj = Profile.objects.filter(user=request.user).first()
        obj.age = age
        obj.weight = weight
        obj.height = height
        obj.sex = sex

        obj.save()

        return redirect("dashboard")
    else:
        obj = Profile.objects.filter(user=request.user).first()

        context = {
            "title": "Daily Miles",
            "sex": obj.sex,
            "age": obj.age,
            "height": obj.height,
            "weight": obj.weight,
        }

        return render(request, "accounts/data.html", context)


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")

    obj = Profile.objects.filter(user=request.user).first()

    context = {
        "title": "Daily Miles",
        "sex": obj.sex,
        "age": obj.age,
        "height": obj.height,
        "weight": obj.weight,
        "bmi": "None",
        "verdict": "None",
    }

    if obj.height and obj.weight:
        context["bmi"] = obj.weight / (obj.height * obj.height)

        if context["bmi"] < 18.5:
            context["verdict"] = "Underweight"
        elif context["bmi"] < 25:
            context["verdict"] = "Healthy Weight"
        elif context["bmi"] < 30:
            context["verdict"] = "Overweight"
        else:
            context["verdict"] = "Obesity"

    return render(request, "accounts/dashboard.html", context)


def trainingMode(request):
    context = {
        "title": "Daily Miles",
    }

    return render(request, "accounts/training.html", context)


def prescription(request):
    context = {
        "title": "Daily Miles",
    }
    return render(request, "accounts/prescription.html", context)
