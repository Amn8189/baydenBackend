from django.shortcuts import render
from .models import Event, Subscriber
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



#csrf - cross site request forgery
"""-----Types of HTTP methods-----"""
#1. GET REQUEST -- requestions to recieve data
#2. POST REQUEST -- SENDING DATA
#3. PUT REQUEST -- CHANGING DATA
#4. DELETE REQUEST -- remove data