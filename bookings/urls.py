from django.urls import path
from .views import CreateBookingView, BookingListView, BookingUpdateView, BookingDeleteView


urlpatterns = [
    path('bookings/new/', CreateBookingView.as_view(), name='booking_new'),
    path('bookings/update/<int:pk>-16584163510635416/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/manage/', BookingListView.as_view(), name='booking_list'),
    path('bookings/delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_confirm_delete'),
]