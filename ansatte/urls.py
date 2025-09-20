from django.urls import path
from . import views

app_name = "ansatte"

urlpatterns = [
    path("", views.index, name="index"),         # liste over ansatte
    path("ny/", views.registrer, name="registrer"),  # registrer ny ansatt
]
