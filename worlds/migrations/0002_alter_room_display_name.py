# Generated by Django 4.2 on 2024-06-10 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='display_name',
            field=models.CharField(choices=[('MEDCAS', 'MEDIEVAL CASTLE'), ('RENVIL', 'RENAISSANCE VILLA'), ('VICMAN', 'VICTORIAN MANSION'), ('DRACAS', 'DRACULA CASTLE'), ('FAIFOR', 'FAIRY FOREST')], max_length=100),
        ),
    ]
