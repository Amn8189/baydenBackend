from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)

class Attendee(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    event = models.ForeignKey(Event, models.CASCADE)

class Subscriber(models.Model):
    firstname = models.CharField(max_length=20)
    secondname = models.CharField(max_length=20)
    email = models.EmailField()
