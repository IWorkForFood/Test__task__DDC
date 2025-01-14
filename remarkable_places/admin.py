from django.contrib import admin
from remarkable_places.models import RemarkablePlace, WeatherSummary
from django_admin_geomap import ModelAdmin
# Register your models here.

class RPAdmin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_autozoom = "10"

class WSAdmin(admin.ModelAdmin):

    readonly_fields = [
        field.name for field in WeatherSummary._meta.fields if field.name != 'id'
        ]
    list_filter = ['remarkable_place__name', 'timestamp']

admin.site.register(RemarkablePlace, RPAdmin)
admin.site.register(WeatherSummary, WSAdmin)