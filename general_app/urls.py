from django.urls import path

from general_app.views import api_root

app_name = 'showtimes_app'

urlpatterns = [
    path('', api_root, name='general_view'),
]
