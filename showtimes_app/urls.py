from django.urls import path

from showtimes_app.views import CinemaListView, CinemaView, ScreeningListView, ScreeningView

app_name = 'showtimes_app'

urlpatterns = [
    path('cinemas/', CinemaListView.as_view(), name='cinema_list_view'),
    path('cinemas/<int:pk>/', CinemaView.as_view(), name='cinema_view'),
    path('screenings/', ScreeningListView.as_view()),
    path('screenings/<int:pk>/', ScreeningView.as_view()),
]
