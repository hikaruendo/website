from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact

import requests,json


def index(request):
    if request.method =="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)

        json_data = json.loads(r.text)
        joke=json_data.get('value').get('joke')
        context={'joker':joke}
        return render(request, 'mysite/index.html',context)
    
    else:
        firstname='hikaru'
        lastname='endo'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)

        json_data = json.loads(r.text)
        joke= json_data.get('value').get('joke')
        context={'joker':joke}
        return render(request, 'mysite/index.html',context)

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