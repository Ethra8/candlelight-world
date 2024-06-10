from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from worlds.views import RoomList


urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('<slug:slug>/', views.room_details, name='room_details'),
]