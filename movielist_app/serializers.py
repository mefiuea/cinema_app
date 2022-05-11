from rest_framework import serializers
from movielist_app.models import Movie, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Person.objects.all())
    director = serializers.SlugRelatedField(slug_field='name', queryset=Person.objects.all())

    class Meta:
        model = Movie
        fields = ("id", "title", "year", "description", "director", "actors")
