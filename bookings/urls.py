from django.urls import path
from .views import CreateBookingView, BookingListView, BookingUpdateView


urlpatterns = [
    path('bookings/new/', CreateBookingView.as_view(), name='booking_new'),
    path('bookings/update/<int:pk>/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/manage/', BookingListView.as_view(), name='booking_list'),
]