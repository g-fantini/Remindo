from django.shortcuts import render

from django.http import HttpResponse

def index(response):
   return render(response,"remindo/base.html",{"name":"y"})

def home(response):
    return render(response,"remindo/home.html",{"name":"x"})