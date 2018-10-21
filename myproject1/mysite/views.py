from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Contact
import requests,json

def home(request):
    if request.method=="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)

        json_data = json.loads(r.text)
        joke=json_data.get('value').get('joke')
        context={'joker':joke}
        return render(request, 'mysite/home.html',context)
    
    else:
        firstname='hikaru'
        lastname='endo'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)

        json_data = json.loads(r.text)
        joke= json_data.get('value').get('joke')
        context={'joker':joke}
        return render(request, 'mysite/home.html',context)


def contact(request):
    if request.method == "POST":
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        c=Contact(email=email, subject=subject, message=message)
        c.save()

        return render(request,'mysite/contact.html')

    else:
        return render(request, 'mysite/contact.html')

def about(request):
    return render(request,'mysite/about.html')