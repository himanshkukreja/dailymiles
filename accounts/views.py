from django.shortcuts import render, HttpResponse, redirect

def home(request):
    context = {
        "title": "Daily Miles"
    }
    return render(request, 'accounts/home.html', context)

def login(request):
    context = {
        "title": "Daily Miles",
    }
    return render(request, "accounts/login.html", context)