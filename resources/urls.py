from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path('backend+resourses/',views.backend_resourses,name="backendR"),
    path('c++-resourses/',views.C_lang_resourses,name="C_langR"),
    path('career+opportunities/',views.career_opportunities,name="career"),
    path('frontend+resourses/',views.frontend_resourses,name="frontendR"),
    path('java+resourses/',views.java_resourses,name="javaR"),
    path('python+resourses/',views.python_resourses,name="pythonR"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)