from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from .models import Contact

def home(request):
    return render(request,'mysite/home.html')

def contact(request):
    if request.method == "POST":
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        c=Contact(email=email, subject=subject, message=message)
        c.save()

        return render(request,'mysite/getback.html')

    else:
        return render(request, 'mysite/contact.html')

def about(request):
    return render(request,'mysite/about.html')