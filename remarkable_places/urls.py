from django.urls import path
from remarkable_places.views import fetch_data_for_all_districts

urlpatterns = [
    path('get_meteo/', fetch_data_for_all_districts, name='get_meteo'),
]
