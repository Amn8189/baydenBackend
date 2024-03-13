from django.shortcuts import render
from .models import Event, Subscriber, Attendee
from django.http import HttpResponse, HttpRequest
from .forms import SubscriberForm, AttendeeForm

# Create your views here.
def homepage(request):
    all_events = Event.objects.all()
    return render(request=request, template_name="homepage.html",
                  context={"all_events":all_events})

def index(request : HttpRequest):
    #get all events
    if request.method == "GET":
        all_events = Event.objects.all()
        context = {"events": all_events}
        #return them in the HTML
        return render(request=request, template_name="index.html",
                      context=context)
    elif request.method == "POST":
        data = {"firstname": request.POST.get("first_name"),
                "secondname": request.POST.get("second_name"),
                "email": request.POST.get("email")}
        
        form_from_subscriber = SubscriberForm(data=data)

        if form_from_subscriber.is_valid():
            new_subscriber = Subscriber()
            new_subscriber.firstname = form_from_subscriber.cleaned_data["firstname"]
            new_subscriber.secondname = form_from_subscriber.cleaned_data["secondname"]
            new_subscriber.email = form_from_subscriber.cleaned_data["email"]
            new_subscriber.save()

        #return them in the HTML
        return render(request=request, template_name="index.html")


def reserve(request : HttpRequest):
    if request.method == "GET":
        return render(request=request, template_name="reserve.html")
    elif request.method == "POST":
        data = {"firstname" : request.POST.get("firstname"),
                "lastname" : request.POST.get("lastname"),
                "email" : request.POST.get("email"),
                "company_name" : request.POST.get("company_name"),
                "country" : request.POST.get("country"),
                "job_title" : request.POST.get("job_title"),
                "phone_number" : request.POST.get("phone_number"),
                "gender" : request.POST.get("gender")}
        new_attendee = AttendeeForm(data=data)
        print(new_attendee.is_valid())
        if new_attendee.is_valid():
            attendee = Attendee()
            Attendee.firstname =  new_attendee.cleaned_data["firstname"]
            Attendee.secondname =  new_attendee.cleaned_data["secondname"]
            Attendee.email =  new_attendee.cleaned_data["email"]
            Attendee.gender =  new_attendee.cleaned_data["gender"]
            Attendee.country =  new_attendee.cleaned_data["country"]
            Attendee.phonenumber =  new_attendee.cleaned_data["phonenumber"]
            Attendee.job_title =  new_attendee.cleaned_data["job_title"]
            Attendee.event =  new_attendee.cleaned_data["event"]

        return render(request=request, template_name="reserve.html")










#csrf - cross site request forgery
"""-----Types of HTTP methods-----"""
#1. GET REQUEST -- requestions to recieve data
#2. POST REQUEST -- SENDING DATA
#3. PUT REQUEST -- CHANGING DATA
#4. DELETE REQUEST -- remove data