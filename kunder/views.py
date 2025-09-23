from django.shortcuts import render, redirect, get_object_or_404
from .models import Kunde
from .forms import KundeForm

# Viser en liste over alle kunder
def kunde_liste(request):
    kunder = Kunde.objects.all().order_by("navn")
    return render(request, "kunder/kunde_liste.html", {"kunder": kunder})

# Registrer ny kunde
def kunde_ny(request):
    if request.method == "POST":
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("kunder:kunde_liste")
    else:
        form = KundeForm()
    return render(request, "kunder/kunde_form.html", {"form": form, "tittel": "Ny kunde"})

# Endre eksisterende kunde
def kunde_endre(request, id):
    kunde = get_object_or_404(Kunde, id=id)
    if request.method == "POST":
        form = KundeForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            return redirect("kunder:kunde_liste")
    else:
        form = KundeForm(instance=kunde)
    return render(request, "kunder/kunde_form.html", {"form": form, "tittel": "Endre kunde"})

# Slette en kunde
def kunde_slette(request, id):
    kunde = get_object_or_404(Kunde, id=id)
    if request.method == "POST":
        kunde.delete()
        return redirect("kunder:kunde_liste")
    return render(request, "kunder/kunde_slette.html", {"kunde": kunde})
