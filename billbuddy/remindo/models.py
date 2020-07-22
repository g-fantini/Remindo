from django.db import models
from django.conf import settings
from celery.worker.strategy import default

class Reminders(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    delivery_time = models.DateTimeField()
    
    SENT_LOG = [("SEN","Sent"),("FOC","Out Of Credit"),("FID","Invalid Destination"),("SCD","Scheduled")]
    sent = models.CharField(max_length=3, choices=SENT_LOG, default="SCD")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminder_receiver')
    #This field is unnecessary at the moment, but has been defined for facilitate future development
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminder_sender')
    
    def __srt__(self):
        return self.title + " " + self.delivery_time
        