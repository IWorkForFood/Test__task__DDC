from django.shortcuts import render
from NewsProject.tasks import fetch_data_for_district
from remarkable_places.models import RemarkablePlace
from remarkable_places.models import WeatherSummary
from django.http import JsonResponse
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

    context = {
        'remarkable_places': remarkable_places,
    }
    
    return render(request, 'remarkable_places/places_info.html', context)