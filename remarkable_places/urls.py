from django.urls import path
from remarkable_places.views import fetch_data_for_all_districts, get_all_places

urlpatterns = [
    path('get_meteo/', fetch_data_for_all_districts, name='get_meteo'),
    path('get_places/', get_all_places, name='get_all_places'),
]
