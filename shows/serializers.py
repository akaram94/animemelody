from rest_framework import serializers
from shows.models import Show, Theme

class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = ('mal_id', 'name', 'year', 'season')


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = ('name', 'show', 'show_name', 'theme_type', 'url', 'priority', 'notes')
    