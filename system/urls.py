#
from django.urls import path
from . import views

urlpatterns = [
    # Midlertidig placeholder – legg til ekte views senere
    path("", views.index, name="index"),
]
