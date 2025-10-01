from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('api/gdrive/list/', list_drive_files, name='gdrive_list'),
]
