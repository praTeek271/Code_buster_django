from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from code_buster.settings import ID,TOKEN
# from django.core.mail import send_mail

import os
from twilio.rest import Client


# Create your views here.

def login_home(request):
    return(render(request, 'login/index.html'))


def signin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return(render(request,'code_busters/index.html',{'username':user.username,'id':user.id}))
        else:
            messages.error(request,'Wrong Credentials')
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
            messages.error(request,"This email is already registered")
            return(redirect('main_homepage'))

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.phoneno=phoneno

        myuser.save()

        messages.success(request,"Successfully logged in")
        

        #<-------- sending Email ----------->
        # subject="Welcome to Code Busters, WebLogin"
        message="Welcome to Code Busters, WebLogin\nHello {0}\t!!\n Please join our discord comunity '''{1}'''".format(myuser.first_name,email_content)
        # from_email=settings.EMAIL_HOST_USER
        # to_email=myuser.email
        to_phoneno=myuser.phoneno
        # send_mail(subject,message,from_email,to_email,)
        send_whatsapp(message,to_phoneno)

        return(redirect("main_homepage"))

    return(render(request, 'login/signup.html'))
    
def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")

    return(redirect('main_homepage'))
    

# # def send_whatsapp(msg,to_phoneno):
# #     client = Client(ID, TOKEN)  
 
# #     message = client.messages.create( 
# #                                 from_='whatsapp:+14155238886',  
# #                                 body=msg,      
# #                                 to='whatsapp:+91'+str(to_phoneno)
# #                             ) 
    
# #     print(message.sid)
     


    
    # message = Mail(
    # from_email=from_email,
    # to_emails=to_email,
    # subject=subject,
    # html_content=msg)

    # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    # response = sg.send(message)
    # print(response.status_code, response.body, response.headers)


email_content='''\n\n<iframe src="https://discord.com/widget?id=789008145245536259&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe> '''
