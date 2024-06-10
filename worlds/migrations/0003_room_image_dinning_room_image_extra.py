# Generated by Django 4.2 on 2024-06-10 18:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0002_alter_room_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image_dinning',
            field=cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='image_extra',
            field=cloudinary.models.CloudinaryField(default='image', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
