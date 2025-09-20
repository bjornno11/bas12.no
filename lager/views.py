from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Forside for Lager</h1><p>Her kommer lagerfunksjoner.</p>")
