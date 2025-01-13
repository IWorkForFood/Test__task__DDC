from News.models import NewsModel
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget

class NewsModelForm(ModelForm):
    
    class Meta:
        model = NewsModel
        fields = ['title', 'main_image', 'image_preview', 'text']
        widgets = {'text': SummernoteWidget()}