from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from datetime import timedelta
from constance import config

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProject.settings')

app = Celery('NewsProject')
app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/Moscow')

# Using Redis as the broker for Celery
app.config_from_object(settings, namespace='CELERY')

email_send_time = config.EMAIL_SEND_TIME
meteosend_time = config.METEO_SEND_TIME

email_send_hour, email_send_minute = [int(x) for x in email_send_time.split(":")] 
meteo_interval_hours, meteo_interval_minute = [int(x) for x in meteosend_time.split(":")] 

#Celery Beat Settings
app.conf.beat_schedule = {
    'send-my-news':{
        'task': 'NewsProject.tasks.send_news_list',
        'schedule': crontab(hour=email_send_hour, minute=email_send_minute),
       # 'args': ()
    },
    'get-meteo-data':{
        'task': 'NewsProject.tasks.fetch_data_for_all_districts',
        'schedule': timedelta(hours=meteo_interval_hours, minutes=meteo_interval_minute),
       # 'args': ()
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()  

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
