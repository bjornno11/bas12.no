from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),        # rot -> landingssiden
    path("about/", views.about, name="about"),      # eksempel på undersider
    path("contact/", views.contact, name="contact")
]
