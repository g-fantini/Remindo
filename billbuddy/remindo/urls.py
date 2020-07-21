# urls.py
from django.urls import path, include

from . import views
from register import views as v
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='index'),
    path("createReminder/", views.createReminder, name="createReminder"),
    path("remindersList/", views.listReminder, name="remindersList"),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),   
]