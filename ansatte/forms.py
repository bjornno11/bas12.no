from django import forms
from django.contrib.auth.models import User
from .models import Ansatt, Rolle


class AnsattUserForm(forms.ModelForm):
    # Felter fra User
    username = forms.CharField(
        max_length=150,
        label="Brukernavn",
        widget=forms.TextInput(attrs={'autocomplete': 'off'})  # 🔹 hindrer autofyll
    )
    first_name = forms.CharField(max_length=30, label="Fornavn")
    last_name = forms.CharField(max_length=30, label="Etternavn")
    email = forms.EmailField(
        required=True,
        label="E-post",
        widget=forms.EmailInput(attrs={'autocomplete': 'off'})  # 🔹 hindrer autofyll
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),  # 🔹 hindrer autofyll
        label="Passord"
    )

    class Meta:
        model = Ansatt
        fields = [
            "username", "first_name", "last_name", "email", "password",  # 👈 Viktig: disse må være med
            "roller", "aktiv",
            "adresse", "telefon",
            "personnummer", "ansatt_dato", "kjonn",
        ]

    def save(self, commit=True):
        # Opprett User først
        username = self.cleaned_data["username"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        # Opprett Django User-objekt
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Opprett Ansatt-objekt og knytt til bruker
        ansatt = super().save(commit=False)
        ansatt.user = user
        if commit:
            ansatt.save()
            self.save_m2m()
        return ansatt


class RolleForm(forms.ModelForm):
    class Meta:
        model = Rolle
        fields = ['navn', 'beskrivelse', 'aktiv']
