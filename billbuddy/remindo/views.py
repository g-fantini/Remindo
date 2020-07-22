from django.shortcuts import render, redirect
from .forms import CreateReminderForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reminders
from bottle import request
from remindo.tasks import send_reminder
from django.utils import timezone
from .redis_connection import *
import datetime
import socket   

def home(response):
    #get the visitor ip address
    IPAddr = socket.gethostbyname(socket.gethostname())  
    
    #add it to redis
    live_counter = add_visit(IPAddr, response.build_absolute_uri())
    
    return render(response,"remindo/home.html",{"counter":live_counter})

def createReminder(response):     
    #Check if user is authenticated otherwise redirect to login
    if not response.user.is_authenticated:
        return redirect("/login") 
    
    if response.method == "POST":
        form = CreateReminderForm(response.POST)
    
        #if form is valid create the record
        if form.is_valid():
            title = form.cleaned_data["title"] 
            message = form.cleaned_data["message"] 
            delivery_time = form.cleaned_data["delivery_time"] 
            current_user = response.user.id
                
            reminder = Reminders(title=title, message=message, delivery_time=delivery_time, sender_id=current_user, receiver_id=current_user  )
            reminder.save()
            
            #here could be possible to add the reminder in celery using
            #send_reminder().delay
            #temporary skipped since using cronjob logic
            
            return HttpResponseRedirect("/remindersList")      
    else:
        form = CreateReminderForm()
    return render(response, "remindo/create_reminder.html", {"form":form})

def listReminder(response):
    #Check if user is authenticated otherwise redirect to login
    if not response.user.is_authenticated:
        return redirect("/login") 
 
    if response.user.is_superuser:
        #allow to an admin user to see all the reminders
        #(a better way would be to use the admin panel)
        reminders = Reminders.objects.filter().order_by('-delivery_time')
    else:
        #get all reminders for the logged in user and sort them by date
        reminders = Reminders.objects.filter(receiver=response.user.id).order_by('-delivery_time')

    return render(response, "remindo/list_reminder.html", {"reminders":reminders})
