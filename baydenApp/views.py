from django.shortcuts import render
from .models import Event
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    all_events = Event.objects.all()
    print(all_events)
    return render(request=request, template_name="homepage.html",
                  context={"all_events":all_events})