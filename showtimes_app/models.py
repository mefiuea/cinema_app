from django.db import models

from movielist_app.models import Movie


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, through='Screening')

    def __str__(self):
        return self.name


class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
