from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from worlds.views import ExperienceList


urlpatterns = [
    path('', views.ExperienceList.as_view(), name='home'),
]