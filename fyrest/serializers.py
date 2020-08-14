from rest_framework import serializers
from .models import GeeksModel, NewsContent

##
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')

class NewsContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ('id', 'headline', 'body')
