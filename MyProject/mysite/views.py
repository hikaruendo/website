from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact


def index(request):
    return render(request, 'mysite/index.html')

def about(request):
    return render(request, 'mysite/about.html')

def contact(request):
    if request.method == "POST":
        email=request.POST.get('email')
        subject=request.POST.get("subject")
        message=request.POST.get('message')
        c=Contact(email=email, subject=subject, message=message)
        c.save()

        return render(request, 'mysite/getback.html')
    else:
        return render(request, 'mysite/contact.html')

def home(request):
    return render(request, 'mysite/home.html')