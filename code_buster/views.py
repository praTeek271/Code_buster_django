from django.shortcuts import render
from django.http import HttpResponse
from resources.models import Team
from datetime import datetime
from resources.models import FeedBack as feed
from django.contrib import messages

def feedBackUs(name,email,subject,msg):
   
    feedback=feed(name=name,email=email,subject=subject,desc=msg,date=datetime.now())
    feedback.save()


def index(request):
    users=Team.objects.all()    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        msg=request.POST.get("message")
        feedBackUs(name, email, subject, msg)
        messages.success(request,"Thanks for your Feadback")

    return(render(request, 'code_busters/index.html',{'team':users}))