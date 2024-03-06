from django.urls import path
from .views import homepage, index

#Transforming method to url
urlpatterns = [
    path("test/", homepage, name="homepage"),
    path("", index, name="index")
]