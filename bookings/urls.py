from django.urls import path
from .views import CreateBookingView

urlpatterns = [
    path('bookings/new/', CreateBookingView.as_view(), name='booking_new'),
]