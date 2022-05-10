from django.urls import path

from showtimes_app.views import CinemaListView, CinemaView

app_name = 'showtimes_app'

urlpatterns = [
    path('cinemas/', CinemaListView.as_view(), name='cinema_list_view'),
    path('cinemas/<int:pk>/', CinemaView.as_view(), name='cinema_view'),
]
