from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Forside for Faste data</h1><p>Her kommer grunnregister (kunder, leverandører, artikler).</p>")
