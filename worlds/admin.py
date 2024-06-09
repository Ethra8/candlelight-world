from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Room

# Register your models here.

@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    list_display = ('id', 'slug', 'image', 'category', 'description')
    prepopulated_fields = {'slug': ('category',)}
    search_fields = ['category', 'id']
    summernote_fields = ('description')