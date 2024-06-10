# Generated by Django 4.2 on 2024-06-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.CharField(choices=[('10:00', '10:00 AM - 04:00 PM'), ('18:00', '06:00 PM - 08:00 AM')], max_length=5),
        ),
    ]
