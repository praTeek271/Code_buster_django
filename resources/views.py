from django.shortcuts import render

# Create your views here.

def backend_resourses(request):
    return(render(request,'resources/backend-resourses.html'))

def C_lang_resourses(request):
    return(render(request,'resources/c++-resourses.html'))

def career_opportunities(request):
    return(render(request,'resources/career-opportunities.html'))

def frontend_resourses(request):
    return(render(request,'resources/frontend-resourses.html'))

def java_resourses(request):
    return(render(request,'resources/java-resourses.html'))

def python_resourses(request):
    return(render(request,'resources/python-resourses.html'))