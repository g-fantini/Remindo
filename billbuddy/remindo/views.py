from django.shortcuts import render, redirect
from .forms import CreateReminderForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reminders
from bottle import request
from remindo.tasks import send_reminder

def home(response):
    return render(response,"remindo/home.html",{})

def createReminder(response):     
    #Check if user is authenticated otherwise redirect to login
    if not response.user.is_authenticated:
        return redirect("/login") 
    
    if response.method == "POST":
        form = CreateReminderForm(response.POST)
    
        if form.is_valid():
            title = form.cleaned_data["title"] 
            message = form.cleaned_data["message"] 
            delivery_time = form.cleaned_data["delivery_time"] 
            current_user = response.user.id
                
            reminder = Reminders(title=title, message=message, delivery_time=delivery_time, sender_id=current_user, receiver_id=current_user  )
            reminder.save()
                
            return HttpResponseRedirect("/remindersList")      
    else:
        form = CreateReminderForm()
    
    return render(response, "remindo/create_reminder.html", {"form":form})

def listReminder(response):
    #Check if user is authenticated otherwise redirect to login
    if not response.user.is_authenticated:
        return redirect("/login") 

    #get all reminders and sort them by date
    reminders = Reminders.objects.filter().order_by('-delivery_time')

    return render(response, "remindo/list_reminder.html", {"reminders":reminders})

def celery(request):
    send_reminder.delay()
    return HttpResponse("")
