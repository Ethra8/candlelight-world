from django.db import models
from django.contrib.auth import get_user_model


TIME_SLOTS = [
    ('10:00', '10:00 AM - 04:00 PM'),
    ('18:00', '06:00 PM - 08:00 AM'),
]

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.CharField(max_length=5, choices=TIME_SLOTS)
    room = models.ForeignKey('worlds.Room', on_delete=models.CASCADE)
    

    def get_absolute_url(self):
        return f"/bookings/{self.id}/"

    def __str__(self):
        return f'Booking {self.id} - {self.user.username} - {self.room.display_name} - {self.date} - {self.get_start_time_display()}'