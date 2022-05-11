from django.urls import path

from movielist_app.views import MovieListView, MovieView, PersonView

app_name = 'movielist_app'

urlpatterns = [
    path('person/', PersonView.as_view(), name='person_view'),
    path('movies/', MovieListView.as_view(), name='movie_list_view'),
    path('movies/<int:pk>/', MovieView.as_view(), name='movie_view'),
]
