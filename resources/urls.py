from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include, re_path
from . import views
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('backend+resourses/',views.backend_resourses,name="backendR"),
    path('c++-resourses/',views.C_lang_resourses,name="C_langR"),
    path('career+opportunities/',views.career_opportunities,name="career"),
    path('frontend+resourses/',views.frontend_resourses,name="frontendR"),
    path('java+resourses/',views.java_resourses,name="javaR"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('python+resourses/',views.python_resourses,name="pythonR"),
]