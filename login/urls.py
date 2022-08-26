from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login_home,name="login_home"),
    path('sign+up', views.signup,name="signup"),
    path('sign+in', views.signin,name="signin"),
    path('sign+out', views.signout,name="signout"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
