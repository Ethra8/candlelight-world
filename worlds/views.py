from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
# from django.http import HttpResponseRedirect
from .models import Room


# Create your views here.
class ExperienceList(generic.ListView):
    queryset = Room.objects.all() #.order_by("created_on")
    template_name = "worlds/index.html"
