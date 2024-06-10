# Generated by Django 4.2 on 2024-06-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0004_alter_room_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='display_name',
            field=models.CharField(choices=[('MEDIEVAL CASTLE', 'medieval-castle'), ('RENAISSANCE VILLA', 'renaissance-villa'), ('VICTORIAN MANSION', 'victorian-mansion'), ('DRACULA CASTLE', 'dracula-castle'), ('FAIRY FOREST', 'fairy-forest')], max_length=100),
        ),
    ]