from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Booking
from .forms import BookingForm


class CreateBookingView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        temp_booking = form.save(commit=False)
        # check if time/ date is available
        existing_bookings = Booking.objects\
            .filter(date=temp_booking.date)\
            .filter(start_time=temp_booking.start_time)\
            .filter(room=temp_booking.room)
            
        if existing_bookings :
            messages.warning(self.request, f'At {temp_booking.start_time} on {temp_booking.date}, our {temp_booking.room} is already booked')
            return redirect(reverse('booking_new'))
        else:
            messages.success(self.request, 'Your booking is confirmed')
            temp_booking.save()
        return redirect(reverse('home'))


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    paginate_by = 1000 # if pagination is desired

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(user=self.request.user)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ["room", "date", "start_time"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        # need to make sure that object that we're updating was created by logged-in user
        if form.instance.user != self.request.user:
            messages.warning(self.request, 'You can only update your own bookings!')
            return redirect(reverse('booking_list'))

        temp_booking = form.save(commit=False)
        # check if time/ date is available
        existing_bookings = Booking.objects\
            .filter(date=temp_booking.date)\
            .filter(start_time=temp_booking.start_time)\
            .filter(room=temp_booking.room)
            
        if existing_bookings :
            messages.warning(self.request, f'At {temp_booking.start_time} on {temp_booking.date}, our {temp_booking.room} is already booked')
            return redirect(f'/bookings/update/{temp_booking.pk}/')
        else:
            messages.success(self.request, "Your booking's changes are confirmed!")
            temp_booking.save()
        return redirect(reverse('home'))