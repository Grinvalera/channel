from django.urls import path

from .views import channel


urlpatterns = [
    path('', channel, name='channel')
]