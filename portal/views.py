from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def public_index(request):
    """Forside for ikke-innloggede brukere"""
    return render(request, "portal/public_index.html")


@login_required
def index(request):
    """Forside for innloggede brukere"""
    return render(request, "portal/index.html")

def index(request):
    return render(request, "portal/index.html")

def landing(request):
    return render(request, "portal/landing.html")

def about(request):
    return render(request, "portal/about.html")

def contact(request):
    return render(request, "portal/contact.html")

def forside(request):
    return render(request, "portal/forside.html")
