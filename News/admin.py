from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from News.models import NewsModel

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(NewsModel, PostAdmin)