from django.urls import path
from remarkable_places.views import (fetch_data_for_all_districts,
                                    get_all_places,
                                    export_weather_summary_to_xlsx)

urlpatterns = [
    path('get_meteo/', fetch_data_for_all_districts, name='get_meteo'),
    path('get_places/', get_all_places, name='get_all_places'),
    path('export-weather-summary/', export_weather_summary_to_xlsx, name='export_weather_summary'),
]
