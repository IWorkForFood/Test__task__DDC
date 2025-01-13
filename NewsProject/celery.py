from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProject.settings')

app = Celery('NewsProject')

# Using Redis as the broker for Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()  

#Celery Beat Settings
app.conf.beat_shedule = {

}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
'''
app.conf.beat_schedule = {
# create an object for your scheduling your task
    'fetch-and-store-temp-data-contrab': {
        'task': 'apilist.tasks.fetch_and_store_temperature', #app_name.tasks.function_name
        'schedule': crontab(minute='*/15'), #crontab() means run every minute
        # 'args' : (..., ...) In case function takes parameters, add them here
    }
}
'''