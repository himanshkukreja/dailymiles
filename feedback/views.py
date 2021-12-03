from django.shortcuts import render,HttpResponse, redirect

def feedback(request):
    context = {
        "title": "Daily Miles Feedback"
    }
    return render(request, 'feedback/feedback.html', context)

# Create your views here.
