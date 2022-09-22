from django.shortcuts import render
from django.http import HttpResponse
from resources.models import Team
# from django.conf import settings
# from django.core.mail import send_mail

def index(request):
    users=Team.objects.all()    
    # subject = 'welcome to GFG world'
    # message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [user.email, ]
    # send_mail( subject, message, email_from, recipient_list )

    return(render(request, 'code_busters/index.html',{'team':users}))