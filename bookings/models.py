from django.db import models
from django.contrib.auth import get_user_model


TIME_SLOTS = [
    ('08:00', '08:00 - 12:00 AM'),
    ('12:00', '12:00 - 04:00 PM'),
    ('16:00', '04:00 - 08:00 PM'),
    ('20:00', '08:00 PM - 12:00 AM'),
]

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.CharField(max_length=5, choices=TIME_SLOTS)
    room = models.ForeignKey('worlds.Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'Booking {self.id} - {self.user.username} - {self.table.display_name} - {self.date} - {self.get_start_time_display()}'