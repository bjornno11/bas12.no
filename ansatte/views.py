from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.models import User
from .models import Ansatt, Rolle
from .forms import AnsattUserForm, RolleForm


# ---------- VIEWS ----------

# Forside for ansatte
def index(request):
    ansatte = Ansatt.objects.all()
    return render(request, "ansatte/index.html", {"ansatte": ansatte})

# Registrere ny ansatt
def registrer(request):
    if request.method == "POST":
        form = AnsattUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ansatte:index")
    else:
        form = AnsattUserForm()
    return render(request, "ansatte/registrer.html", {"form": form})


# ---------- ROLLER ----------

# Liste alle roller
def rolle_liste(request):
    roller = Rolle.objects.all().order_by('navn')
    return render(request, 'ansatte/roller_liste.html', {'roller': roller})

# Opprette ny rolle
def rolle_ny(request):
    if request.method == 'POST':
        form = RolleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ansatte:rolle_liste')
    else:
        form = RolleForm()
    return render(request, 'ansatte/rolle_form.html', {'form': form, 'tittel': 'Ny Rolle'})

# Endre eksisterende rolle
def rolle_endre(request, id):
    rolle = get_object_or_404(Rolle, id=id)
    if request.method == 'POST':
        form = RolleForm(request.POST, instance=rolle)
        if form.is_valid():
            form.save()
            return redirect('ansatte:rolle_liste')
    else:
        form = RolleForm(instance=rolle)
    return render(request, 'ansatte/rolle_form.html', {'form': form, 'tittel': 'Endre Rolle'})

# Slette en rolle
def rolle_slette(request, id):
    rolle = get_object_or_404(Rolle, id=id)
    if request.method == 'POST':
        rolle.delete()
        return redirect('ansatte:rolle_liste')
    return render(request, 'ansatte/rolle_slette.html', {'rolle': rolle})
