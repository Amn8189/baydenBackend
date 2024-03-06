from django.contrib import admin
from .models import Event, Attendee, Subscriber

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ("name",)

class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee
    list_display = ("firstname", "email")

class SubscriberAdmin(admin.ModelAdmin):
    model = Subscriber
    list_display = ("firstname", "firstname", "email")

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)