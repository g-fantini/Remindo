import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'billbuddy.settings')

app = Celery('billbuddy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#Set chron job to execute the task send_reminder
app.conf.beat_schedule = {
    'send-overduereminders-every-minute': {
        'task': 'tasks.send_reminder',
        'schedule': 60.0,
        'args': ()
    },
}
app.conf.timezone = 'Europe/London'