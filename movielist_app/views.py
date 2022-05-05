from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, viewsets

from movielist_app.serializers import MovieSerializer
from movielist_app.models import Movie


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
