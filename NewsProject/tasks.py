from django.core.cache import cache
from celery import shared_task
import requests

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"