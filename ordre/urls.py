from django.urls import path
from . import views

urlpatterns = [
    path("liste/", views.ordre_liste, name="liste"),
    path("ny/", views.ordre_ny, name="ny"),
    path("", views.index, name="index"),
]
