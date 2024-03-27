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


def reserve(request : HttpRequest, pk):
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
            attendee.firstname =  new_attendee.cleaned_data["firstname"]
            attendee.lastname  =  new_attendee.cleaned_data["lastname"]
            attendee.email =  new_attendee.cleaned_data["email"]
            attendee.gender =  new_attendee.cleaned_data["gender"]
            attendee.country =  new_attendee.cleaned_data["country"]
            attendee.phone_number =  new_attendee.cleaned_data["phone_number"]
            attendee.company_name =  new_attendee.cleaned_data["company_name"]
            attendee.job_title =  new_attendee.cleaned_data["job_title"]
            new_event = Event.objects.get_or_create(pk=pk)[0]
            attendee.event = new_event
            attendee.save()

        return render(request=request, template_name="reserve.html")

from .forms import EventForm
def create_event(request :HttpRequest):
    event_form = EventForm()
    if request.method == "POST":
        event_form = EventForm(request.POST, files=request.FILES)
        if event_form.is_valid():
            event_form.save()
        else:
            print(event_form.errors)

    return render(request=request,
                   template_name="create_event.html",
                   context={"event_form":event_form})



from django.views.generic import CreateView
from .forms import OrganizerCreationForm
from django.urls import reverse_lazy
class SignupView(CreateView):
    form_class = OrganizerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

