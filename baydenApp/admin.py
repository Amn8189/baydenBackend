from django.contrib import admin
from .models import Event, Attendee

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("name")

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee
    list_display = ("firstname", "email")