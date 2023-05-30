from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'original_language', 'backdrop_path', 'overview','popularity','release_date',
                  'poster_path', 'vote_count')
