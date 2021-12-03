from django.shortcuts import render, HttpResponse, redirect

def home(request):
    context = {
        "title": "ML-TOOLBOX"
    }
    return render(request, 'accounts/home.html', context)

