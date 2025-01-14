from django.core.cache import cache
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
import requests
from NewsProject import settings
from News.models import NewsModel
from django.utils import timezone
from constance import config
from remarkable_places.models import RemarkablePlace, WeatherSummary

@shared_task(bind=True)
def send_news_list(self):

    today = timezone.localdate() 
    news_today = NewsModel.objects.filter(publication_date=today)

    if news_today.exists():
        subject = config.EMAIL_SUBJECT
        body = config.EMAIL_BODY 
        recipients = config.EMAIL_RECIPIENTS.split(' ') 

        body += '\n\n'
        for news in news_today:
            body += f"{news.title}\n\n"

        if recipients[0] == '-' and len(recipients) == 1:
            mails = [x.email for x in get_user_model().objects.all()]
            recipients = mails

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

@shared_task
def fetch_data_for_all_districts():
    districts = RemarkablePlace.objects.all()

    for district in districts:
        fetch_data_for_district.delay(district.id)

@shared_task
def fetch_data_for_district(district_id):
    district = RemarkablePlace.objects.get(id=district_id)
    key = '346cbace86834eedaa973417251401'
    district_latitude = district.lat
    district_longitude = district.lon

    api_url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={district_latitude},{district_longitude}'

    response = requests.get(api_url)
    if response.status_code == 200:
        
        data = response.json()['current']
        print(data)

        district_weather = WeatherSummary(temperature = data['temp_c'],
                                          humidity = data['humidity'],
                                          pressure = data['pressure_mb'],
                                          wind_direction = data['wind_dir'],
                                          wind_speed = data['wind_kph']/3.6,
                                          remarkable_place = RemarkablePlace.objects.get(pk = district_id)
                                        )
        district_weather.save()

    else:
        print('ERRORE')


