from django.forms import Form
from django import forms

class SubscriberForm(Form):
    firstname = forms.CharField(max_length=20)
    secondname = forms.CharField(max_length=20)
    email = forms.EmailField()

class AttendeeForm(Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField()
    company_name = forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)
    job_title = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
    gender = forms.CharField(max_length=20)