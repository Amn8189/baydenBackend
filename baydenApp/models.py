from django.db import models

# Create your models here.
class Subscriber(models.Model):
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=20)
    email = models.EmailField()

class Organizer(models.Model):
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Event(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=20, default="")
    time_of_attendance = models.DateTimeField( default="")
    organizer = models.ForeignKey(Organizer, models.CASCADE, default=1)

class Attendee(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20, default="")
    job_title = models.CharField(max_length=20, default="")
    event = models.ForeignKey(Event, models.CASCADE)
