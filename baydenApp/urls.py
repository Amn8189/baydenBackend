from django.urls import path
from .views import homepage

#Transforming method to url
urlpatterns = [
    path("", homepage, name="homepage")
]