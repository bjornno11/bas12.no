from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Forside for Reskontro</h1><p>Her kommer reskontro-funksjoner.</p>")
