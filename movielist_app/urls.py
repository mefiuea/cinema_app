from django.urls import path

from . import views

app_name = 'movielist_app'

urlpatterns = [
    path('', views.api_overview, name='api_overview_view'),
]
