from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.login_home,name="login_home"),
    path('sign+up', views.signup,name="signup"),
    path('sign+in', views.signin,name="signin"),
    path('sign+out', views.signout,name="signout"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
