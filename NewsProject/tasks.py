from django.core.cache import cache
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from NewsProject import settings
from News.models import NewsModel
from django.utils import timezone
from constance import config

@shared_task(bind=True)
def send_news_list(self):

    today = timezone.localdate()  # Получаем текущую дату
    news_today = NewsModel.objects.filter(publication_date=today)

    if news_today.exists():
        subject = config.EMAIL_SUBJECT
        body = config.EMAIL_BODY 
        recipients = config.EMAIL_RECIPIENTS.split(' ') 

        # Формируем тело письма с новостями
        body += '\n\n'
        for news in news_today:
            body += f"{news.title}\n\n"

        if recipients[0] == '-' and len(recipients) == 1:
            mails = [x.email for x in get_user_model().objects.all()]
            print(mails)
            recipients = mails
            print(recipients)

        for email in recipients:
            mail_subject = subject
            message = body
            to_email = email
            send_mail(
                subject = mail_subject,
                message = message,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=[to_email],
                fail_silently=True,
            )
