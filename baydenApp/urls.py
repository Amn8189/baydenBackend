from django.urls import path
from .views import homepage, index, reserve, create_event, SignupView

#Transforming method to url
urlpatterns = [
    path("test/", homepage, name="homepage"),
    path("", index, name="index"),
    path("reserve/<int:pk>", reserve, name="reserve"),
    path("create_event/", create_event, name="create_event"),
    path("signup/", SignupView.as_view(template_name="signup.html"), name="signup"),
]