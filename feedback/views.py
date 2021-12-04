from django.contrib.messages import constants
from django.shortcuts import render, HttpResponse, redirect
import json
from .models import FeedbackMsg
from django.contrib.auth.models import User
from django.contrib import messages


def feedback(request):
    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        msg = request.POST.get("msg")

        user = User.objects.filter(username=request.user).first()
        feedback_obj = FeedbackMsg.objects.create(user=user, msg=msg)
        feedback_obj.save()

        return redirect("login")
    else:
        context = {
            "title": "Daily Miles"
        }

        return render(request, 'feedback/feedback.html', context)

