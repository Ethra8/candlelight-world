from django.urls import path
from .views import CreateBookingView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('bookings/new/', CreateBookingView.as_view(), name='booking_new'),
    # path('bookings/confirm, ')
    path('bookings/<id:id>/', CreateBookingView.as_view(), name='worlds.index'),
]