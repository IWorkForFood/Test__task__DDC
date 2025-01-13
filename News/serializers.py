from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import NewsModel

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = "__all__"
