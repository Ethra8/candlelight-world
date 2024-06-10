from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Room


# Create your views here.
class RoomList(generic.ListView):
    queryset = Room.objects.all()
    template_name = "worlds/index.html"


def room_details(request, slug):
    """
    Display an individual :model:`worlds.Room`.
    **Context**
    ``room``
        An instance of :model:`worlds.Room`.
    
    **Template:**
    :template:`worlds/room_details.html`
    """
    queryset = Room.objects.all()
    room = get_object_or_404(queryset, slug=slug)
    description = get_object_or_404(queryset, description=room.description)

    return render(
        request,
        "worlds/room_details.html",
        {
            "room": room,
            "slug": slug,
            "description": description,
        },
    )
