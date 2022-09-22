from django.shortcuts import render
from .models import Resourses,Team

# Create your views here.
def categorizer(sub):
    res_data=Resourses.objects.all().filter(subject='Java').filter(show='True')   
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
    # print(all_content)
    return(all_content)


def backend_resourses(request):
    all_product={'all_res_content':categorizer('Back-End')}
    return(render(request,'resources/backend-resourses.html',all_product))

def C_lang_resourses(request):
    all_product={'all_res_content':categorizer('C++')}
    return(render(request,'resources/c++-resourses.html',all_product))

def career_opportunities(request):
    all_product={'all_res_content':categorizer('Java')}
    return(render(request,'resources/career-opportunities.html',all_product))

def frontend_resourses(request):
    all_product={'all_res_content':categorizer('Front-End')}
    return(render(request,'resources/frontend-resourses.html',all_product))

def java_resourses(request):
    test=Team.objects.values('user_img')
    for i in test:
        print(i)
    all_product={'all_res_content':categorizer('Java')}
    return(render(request,'resources/java-resourses.html',all_product))

def python_resourses(request):
    all_product={'all_res_content':categorizer('Python')}
    return(render(request,'resources/python-resourses.html',all_product))

def handle404(request,exception):
    return(render(request,'Page_not_found.html'))

def handle500(request):
    return(render(request,'Page_not_found.html'))