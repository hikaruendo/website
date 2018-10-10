from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'mysite/index.html')

def about(request):
    return render(request, 'mysite/about.html')

def contact(request):
    return render(request, 'mysite/contact.html')

def home(request):
    return render(request, 'mysite/home.html')