from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Account


from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from code_buster.settings import ID,TOKEN
# from django.core.mail import send_mail

import os


# Create your views here.

def login_home(request):
    return(render(request, 'login/index.html'))

# add sign in feature
def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return(render(request,'code_busters/index.html',{'username':user.username,'id':user.id}))
        else:
            messages.error(request,"Wrong Credentials")
            # messages.error(request,'')
            return(redirect('main_homepage'))

    return(render(request, 'login/signin.html'))
    
def signup(request):
    if request.method =="POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        password=request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request,"This username is already present")
            return(redirect('main_homepage'))

        if User.objects.filter(email=email):
            messages.warning(request,"This email is already registered")
            return(redirect('main_homepage'))
        try:
           
            myuser=User.objects.create_user(username,email,password,first_name=firstname,last_name=lastname)
        except:
            messages.warning(request,"An Error happened. Try Again")
        try:
            ph=User.objects.get(username=username)
            print('user fetched')
            pph=Account.objects.get(user=ph)
            print('Account fetched')
            pph.phoneno=phoneno
            print('phone no added')
            pph.save()
        except Exception as e:
            print(f"-------------->{e}")
            messages.warning(request,e)

        myuser.save()

        messages.success(request,f"{firstname}'s Account created Successfully !")

        message="Welcome ,{0} to Code Busters,\nHello, Please login to use our services ".format(myuser.first_name)
        messages.success(request,message)        
        return(redirect("main_homepage"))

    return(render(request, 'login/signup.html'))
    
def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")

    return(redirect('main_homepage'))
    

