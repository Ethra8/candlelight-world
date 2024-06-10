from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Room

# Register your models here.

@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    list_display = ('id', 'slug', 'category', 'display_name', 'description', 'image', 'image_dinning', 'image_extra')
    prepopulated_fields = {'slug': ('display_name',)}
    search_fields = ['category']
    summernote_fields = ('description')