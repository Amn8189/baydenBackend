from django.forms import Form, ModelForm, TextInput, FileInput
from django import forms
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'image', 'time_of_attendance']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                "style":"width:200px", 
        }),
            'location': TextInput(attrs={
                'class': 'form-control',
                "style":"width:200px", 
        }),
            'image': FileInput(attrs={
                'class': 'form-control',
                "style":"width:200px", 
        }),
            'time_of_attendance': TextInput(attrs={
                'class': 'form-control',
                "style":"width:200px", 
        }),


        }


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