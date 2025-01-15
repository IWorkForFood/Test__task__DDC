from django import forms
from .models import RemarkablePlace


class XlsxImportForm(forms.Form):
    xlsx_file = forms.FileField()

class DateRangeForm(forms.Form):
    remarkable_place = forms.ChoiceField(choices=RemarkablePlace.objects.values_list('name', 'name'))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))