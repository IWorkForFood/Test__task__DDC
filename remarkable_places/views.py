from django.shortcuts import render
from NewsProject.tasks import fetch_data_for_district
from remarkable_places.models import RemarkablePlace
from remarkable_places.models import WeatherSummary
from django.http import JsonResponse
from openpyxl import Workbook
from django.http import HttpResponse
from datetime import datetime
from .forms import DateRangeForm
# Create your views here.

def fetch_data_for_all_districts(request):
    # Получаем все районы
    districts = RemarkablePlace.objects.all()
    
    # Запускаем задачу для каждого района
    for district in districts:
        fetch_data_for_district.delay(district.id)
    
    return JsonResponse({'status': 'tasks are being processed'})

def get_all_places(request):

    remarkable_places = RemarkablePlace.objects.all()
    form = DateRangeForm(request.GET)

    context = {
        'remarkable_places': remarkable_places,
        'form': form,
    }
    
    return render(request, 'remarkable_places/places_info.html', context)


def export_weather_summary_to_xlsx(request):
    form = DateRangeForm(request.GET)
    
    if request.method == 'GET' and form.is_valid():

        remarkable_place_name = form.cleaned_data['remarkable_place']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        
        weather_summaries = WeatherSummary.objects.filter(
            remarkable_place__name=remarkable_place_name,
            timestamp__range=[start_date, end_date]
        )

        wb = Workbook()
        ws = wb.active
        ws.title = "Weather Summary"

        ws.append(['Примечательное место', 'Дата', 'Температура', 'Влажность', 'Скорость ветра'])

        for summary in weather_summaries:
            ws.append([
                summary.remarkable_place.name,
                summary.timestamp.replace(tzinfo=None),
                summary.temperature,
                summary.humidity,
                summary.wind_speed
            ])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"weather_summary_{timestamp}.xlsx"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        wb.save(response)

        return response

    return render(request, 'remarkable_places/places_info.html', {'form': form})