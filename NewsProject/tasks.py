from django.core.cache import cache
from django.contrib.auth import get_user_model
from celery import shared_task
import requests
from django.core.mail import send_mail
from NewsProject import settings

@shared_task(bind=True)
def send_news_list(self):
    '''
    users = get_user_model().objects.all()
    for user in users:
         mail_subject = "Hi"
         message = "Hello, oy"
         to_email = user.email
         send_mail(
              subject = mail_subject,
              message = message,
              from_email = settings.EMAIL_HOST_USER,
              recipient_list=to_email,
              fail_silently=True,
         )
    '''
    mail_subject = "Hi"
    message = "Hello, oy"
    to_email = "chikovm@bk.ru"
    send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    print("Есть?")
    return "Done"
