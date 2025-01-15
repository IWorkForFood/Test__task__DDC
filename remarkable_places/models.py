from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_admin_geomap import GeoItem

class RemarkablePlace(models.Model, GeoItem):

    name = models.CharField(max_length=255, unique=True) 
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта
    rating = models.PositiveIntegerField( 
        default=3,
        validators=[MinValueValidator(0), MaxValueValidator(25)]
    )

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat is None else str(self.lat)


    def __str__(self):
        return self.name

class WeatherSummary(models.Model):

    temperature = models.FloatField(help_text="Температура в градусах Цельсия")
    humidity = models.IntegerField(help_text="Влажность воздуха в процентах")
    pressure = models.IntegerField(help_text="Атмосферное давление в мм ртутного столба")
    wind_direction = models.CharField(max_length=50, help_text="Направление ветра")
    wind_speed = models.FloatField(help_text="Скорость ветра в м/с")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Дата и время записи")
    remarkable_place = models.ForeignKey(RemarkablePlace, on_delete=models.CASCADE)

    def __str__(self):
        return f"Weather on {self.timestamp}: {self.temperature}°C, {self.wind_speed} m/s"
    
