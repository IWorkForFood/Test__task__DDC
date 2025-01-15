from django import forms
from .models import RemarkablePlace
from django.forms.models import ModelChoiceField

class XlsxImportForm(forms.Form):
    xlsx_file = forms.FileField()

class DateRangeForm(forms.Form):
    remarkable_place = forms.ChoiceField(choices=ModelChoiceField(queryset=RemarkablePlace.objects.all()))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))