from django.urls import path
from .views import homepage, index, reserve

#Transforming method to url
urlpatterns = [
    path("test/", homepage, name="homepage"),
    path("", index, name="index"),
    path("reserve/<int:pk>", reserve, name="reserve")
]