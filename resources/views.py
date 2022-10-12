from django.shortcuts import render
from .models import Resourses,Team,event,FAQ
from django.contrib import messages
from code_buster.views import feedBackUs


# Create your views here.
def res_categorizer(sub):
    res_data=Resourses.objects.all().filter(subject=sub).filter(show='True')
    print(len(res_data))
    all_content=[]
    categories=[]
    cat=[]
    for i in res_data:
        cat.append(i.category)
    cat=[*set(cat)]   # removes dublicate items

    for i in cat:
        temp=res_data.filter(category=i)
        tmp_list=[]
        for tmp in temp:
            tmp_list.append(tmp)
        all_content.append([tmp_list,i])

    
    print(all_content)
    return(all_content)


def backend_resourses(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        msg=request.POST.get("message")
        feedBackUs(name, email, subject, msg)
        messages.success(request,"Thanks for your Feadback")
    all_product={'all_res_content':res_categorizer('Back-End')}
    return(render(request,'resources/backend-resourses.html',all_product))

def C_lang_resourses(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        msg=request.POST.get("message")
        feedBackUs(name, email, subject, msg)
        messages.success(request,"Thanks for your Feadback")
    all_product={'all_res_content':res_categorizer('C++')}
    return(render(request,'resources/c++-resourses.html',all_product))

def career_opportunities(request):
    feadextractor(request)
    # category
    evnt=event.objects.all().filter(show='True')
    print(f"No of Events count -- {len(evnt)}")
    all_content=[]
    categories=[]
    cat=[]
    for i in evnt:
        cat.append(i.category)
    cat=[*set(cat)]   # removes dublicate items

    for i in cat:
        temp=evnt.filter(category=i)
        tmp_list=[]
        for tmp in temp:
            tmp_list.append(tmp)
        all_content.append([tmp_list,i])
    # Faq section 
    ques_query=faq_category('Internship')
    all_product={'all_evnt_content':all_content,'FAQs':ques_query}
    print(all_content)
    return(render(request,'resources/career-opportunities.html',all_product))

def frontend_resourses(request):
    feadextractor(request)
    all_product={'all_res_content':res_categorizer('Front-End')}
    return(render(request,'resources/frontend-resourses.html',all_product))

def java_resourses(request):
    feadextractor(request)
    all_product={'all_res_content':res_categorizer('Java')}
    return(render(request,'resources/java-resourses.html',all_product))

def python_resourses(request):
    feadextractor(request)
    all_product={'all_res_content':res_categorizer('Python')}
    return(render(request,'resources/python-resourses.html',all_product))

def handle404(request,exception):
    return(render(request,'Page_not_found.html'))

def handle403(request,exception):
    return(render(request,'Page_not_found.html'))

def handle500(request):
    return(render(request,'Page_not_found.html'))



def feadextractor(request):

    try:    
        if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            subject=request.POST.get("subject")
            msg=request.POST.get("message")
            feedBackUs(name, email, subject, msg)
            messages.success(request,"Thanks for your Feadback")
    except:
        messages.warning(request,"Sorry ,we couldn't recieve your precious Feedback.\nTry sending them again.")


def faq_category(category):
    ques_query=[]

    ques_queries=FAQ.objects.all().filter(category='Internship').filter(show='True')
    # for i in ques_queries:
    #     ques_query_set.append(i)
    return(ques_query)