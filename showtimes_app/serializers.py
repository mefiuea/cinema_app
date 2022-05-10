from rest_framework import serializers

from showtimes_app.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movielist_app:movie_view')

    class Meta:
        model = Cinema
        fields = ['name', 'city', 'movies']
        