from django.shortcuts import render
from .forms import CreateReminderForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reminders

def home(response):
    return render(response,"remindo/home.html",{})

def createReminder(response):
    if response.method == "POST":
        form = CreateReminderForm(response.POST)

        if form.is_valid():
            title = form.cleaned_data["title"] 
            message = form.cleaned_data["message"] 
            delivery_time = form.cleaned_data["delivery_time"] 
            current_user = response.user.id
            
            reminder = Reminders(title=title, message=message, delivery_time=delivery_time, sender_id=current_user, receiver_id=current_user  )
            reminder.save()
            
            return HttpResponseRedirect("/home")


       

    else:
        form = CreateReminderForm()

    return render(response, "remindo/create_reminder.html", {"form":form})