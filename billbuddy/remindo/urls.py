# urls.py
from django.urls import path, include

from . import views
from register import views as v

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
   
    
]