from __future__ import absolute_import, unicode_literals

from celery.app import shared_task
from django.core.mail import send_mail
from .models import Reminders
from register.models import Profile
from remindo.sms import send
from django.utils import timezone

@shared_task
def send_reminder():
    #get reminder pending in the queue and the relative phone number
    #since at the moment the sender and receiver are the same use the same variable
    reminders_to_send = Reminders.objects.raw('''SELECT title, phone, r.id                 
                                                FROM remindo_reminders r, register_profile p
                                                WHERE r.sender_id = p.user_id AND sent = "SCD" AND delivery_time < strftime('%Y-%m-%d %H-%M','now') 
                                                ORDER BY delivery_time''')
    
    for reminder in reminders_to_send:
        #for each reminder, set the sent field with the relative status
        reminder.sent = send(reminder.phone, reminder.phone, reminder.message)
        reminder.save(update_fields=["sent"] )
    return None