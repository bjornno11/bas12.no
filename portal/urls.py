from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    path("", views.public_index, name="public_index"),  # åpen side
    path("home/", views.index, name="index"),           # innlogget side
]
