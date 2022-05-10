from django.urls import path

from movielist_app.views import MovieListView, MovieView

app_name = 'movielist_app'

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list_view'),
    path('movies/<int:pk>/', MovieView.as_view(), name='movie_view'),
]
