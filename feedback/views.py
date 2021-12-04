from django.contrib.messages import constants
from django.shortcuts import render, HttpResponse, redirect
import json
from .models import feedbackmsg
from django.contrib.auth.models import User
from django.contrib import messages


def feedback(request):
    if request.method == "POST":
        username = request.POST.get("username")
        contact = request.POST.get("contact")
        msg = request.POST.get("msg")

        context = {
            "username": username,
            "contact": contact 
        }

        feedback_obj = User(username=username, contact=contact, msg=msg)

        feedback_obj = feedbackmsg.objects.create(user=user_obj)
        feedback_obj.save()

        return redirect("login")
    else:
        context = {
            "title": "Daily Miles"
        }

        return render(request, 'feedback/feedback.html', context)

