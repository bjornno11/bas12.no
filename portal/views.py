from django.shortcuts import render

def landing(request):
    return render(request, "portal/landing.html")

def about(request):
    return render(request, "portal/about.html")

def contact(request):
    return render(request, "portal/contact.html")
