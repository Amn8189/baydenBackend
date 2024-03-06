from django.shortcuts import render
from .models import Event
from django.http import HttpResponse, HttpRequest
from .forms import SubscriberForm

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
        form_from_subscriber = SubscriberForm()
        

#1. GET REQUEST -- requestions to recieve data
#2. POST REQUEST -- SENDING DATA
#3. PUT REQUEST -- CHANGING DATA
#4. DELETE REQUEST -- remove data