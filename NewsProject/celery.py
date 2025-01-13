from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProject.settings')

app = Celery('NewsProject')
app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Moscow')

# Using Redis as the broker for Celery
app.config_from_object(settings, namespace='CELERY')

#Celery Beat Settings
app.conf.beat_shedule = {
    'send-my-news':{
        'task': 'NewsProject.tasks.send_news_list',
        'schedule': crontab(hour=8, minute=0),
       # 'args': ()
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()  

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
