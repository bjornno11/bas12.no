from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Forside for Ordre/Faktura</h1><p>Her kommer ordre- og fakturafunksjoner.</p>")

def ordre_liste(request):
    return render(request, "ordre/ordre_liste.html")

def ordre_ny(request):
    return render(request, "ordre/ordre_ny.html")
