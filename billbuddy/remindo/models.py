from django.db import models
from django.conf import settings

class Reminders(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    delivery_time = models.DateTimeField()

    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminder_receiver')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminder_sender')
    
    def __srt__(self):
        return self.title + " " + self.delivery_time
    
class Visits(models.Model):
    time = models.DateTimeField()
    ip_address = models.CharField(max_length=32)
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __srt__(self):
        return self.visitor + " " + self.time 
    