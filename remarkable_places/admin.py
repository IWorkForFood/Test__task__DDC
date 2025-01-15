from django.contrib import admin
from remarkable_places.models import RemarkablePlace, WeatherSummary
from django_admin_geomap import ModelAdmin
from django.urls import path
from openpyxl.reader.excel import load_workbook
from django.shortcuts import redirect, render
from remarkable_places.forms import XlsxImportForm

class RPAdmin(ModelAdmin):
    
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_autozoom = "10"

    change_list_template = 'remarkable_places/record_change_list.html' 

    def get_urls(self):

        urls = super().get_urls()
        my_urls = [
            path('import-records-from-xlsx/', self.import_records_from_xlsx),
        ]
        return my_urls + urls
    
    def import_records_from_xlsx(self, request):

        context = admin.site.each_context(request)
        if request.method == 'POST':
            xlsx_file = request.FILES['xlsx_file']

            workbook = load_workbook(filename=xlsx_file, read_only=True)
            worksheet = workbook.active

            records_to_save = []
            for row in worksheet.rows:
                new_obj = self.model(name=row[0].value, lon=row[1].value, lat=row[2].value, rating=row[3].value)
                records_to_save.append(new_obj)
            self.model.objects.bulk_create(records_to_save)

            self.message_user(request, f'Импортировано строк: {len(records_to_save)}.')
            return redirect('admin:remarkable_places_remarkableplace_changelist')

        context['form'] = XlsxImportForm()
        return render(request, 'remarkable_places/add_records_form.html', context=context)

class WSAdmin(admin.ModelAdmin):

    readonly_fields = [
        field.name for field in WeatherSummary._meta.fields if field.name != 'id'
        ]
    list_filter = ['remarkable_place__name', 'timestamp']

    
admin.site.register(RemarkablePlace, RPAdmin)
admin.site.register(WeatherSummary, WSAdmin)