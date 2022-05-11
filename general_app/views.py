from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'person': reverse('movielist_app:person_view', request=request, format=format),
        'movies': reverse('movielist_app:movie_list_view', request=request, format=format),
        'cinemas': reverse('showtimes_app:cinema_list_view', request=request, format=format),
        'screenings': reverse('showtimes_app:screenings_list_view', request=request, format=format),
    })
